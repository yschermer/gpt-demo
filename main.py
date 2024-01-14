#   gcloud functions deploy jcb \
#     --gen2 \
#     --runtime=python310 \
#     --region=europe-west4 \
#     --source=. \
#     --entry-point=jcb \
#     --trigger-http \
#     --allow-unauthenticated

import json
import functions_framework

# @functions_framework.http
# def hue(request):

@functions_framework.http
def jcb(request):
    # parse json from request which contains something like {"input": "some text"}
    request_json = request.get_json()

    # get the input from the json
    input = request_json["input"]

    text = f"""Christopher Columbus undertook several voyages across the Atlantic Ocean which led to the European awareness of the American continents. These journeys were pivotal in the history of exploration and had profound implications on the world history. One of the notable items in our collection that provides insight into Columbus's routes to the Americas is the "Carte des Côtes de Terre-Firme depuis la R. d'Orénoque jusqu'au Yucatan avec les iles Antille et Lucayes où se trouvent les routes suivies par Christophe Colomb dans ces mers lors de ses découvertes." This fold-out engraved map, included in the third volume of Martín Fernández de Navarrete's work from 1828, details the Caribbean islands and delineates the paths taken by Columbus on his four voyages. With clear indications of shallows and dangerous rocks, the map spans from the southern tip of Florida to the eastern parts of Central America and the northern part of South America, illustrating the areas explored by Columbus. Another significant item is "Newe vnbekanthe Landte und ein newe Weldte in kurtz verganger Zeythe erfunden," dating back to 1508 and comprised of accounts of the voyages of Christopher Columbus and Amerigo Vespucci. The compilation delivers narratives from several explorers and includes the Low German translation by Henning Ghetelen of the Italian work, which originally brought to light the tales of new lands being discovered at that time. This early printed book not only discusses Columbus's travels but also broadens the context with descriptions of Vespucci's adventures, offering readers a comprehensive view of early discoveries that reshaped the understanding of the world. Both of these works can offer a historical perspective on the routes and discoveries of Christopher Columbus, complementing the narrative of how these voyages changed the course of global history."""

    return json.dumps({
        "output": text,
        "images": [
            "[Map](https://i.imgur.com/8CdZyHW.png)",
            "[Book](https://i.imgur.com/QXQcz75.png)"
        ],
        "urls_more_info": [
            "https://americana.jcblibrary.org/search/object/jcbcap-ljcbmaps-1-1-6306-115902534/",
            "https://americana.jcblibrary.org/search/object/jcbcap-991008766229706966-newevnbekanthela00unkn/"
        ]
    })