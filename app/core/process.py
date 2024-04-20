
import json
import uuid

from app.core.models import AskResponse
from app.services.gemini import generate_text
from app.services.vision import get_text_from_image
from app.services.youtube import search_youtube_videos
from app.core.prompts import bot_prompt

converstions = {}

def process(query: str, image_content: bytes = None, conversation_id: str = None):
    conversation_history = []
    if conversation_id:
        conversation_history = converstions.get(conversation_id, [])
    else:
        conversation_id = str(uuid.uuid4())

    if image_content:
        image_text = get_text_from_image(content=image_content)
        # append text from image to the end of string query
        query += f"\n{image_text}"

    prompt = bot_prompt(query, conversation_history)

    response = generate_text(prompt)
    
    if response:
        response_json = json.loads(response)
    else:
        raise Exception("Falied to fetch data from llm.")
    
    answer = response_json['answer']
    rephrased_query = response_json['rephrased_query']

    
    links = search_youtube_videos(rephrased_query, 2)
    

    conversation_history.append({
        'Human': query
    })

    conversation_history.append({
        'Bot': answer
    })

    converstions[conversation_id] = conversation_history

    return AskResponse(
        chat_id=str(uuid.uuid4()),
        converstion_id=conversation_id,
        answer=answer,
        contents=links
    )
    


    


    