# 
# Exemplo de como processar dados provenientes de um JSON
#

import urllib.request  
import json

def ManiputaJSON():
    enderecoDoSite = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson';
    WebURL = urllib.request.urlopen(enderecoDoSite);
    
    if(WebURL.getcode() == 200):
        print("URL RECONHECIDA!!!")
        
        dados = WebURL.read();
        oJSON = json.loads(dados);
        
        contagem = oJSON["metadata"]["count"]
        print("Contagem:" + str(contagem))
        
        for local in oJSON["features"]:
            if(local["properties"]["place"] == "106km W of Rockaway Beach, Oregon"):
                print("*****LUGAR ESPECIAL ENCONTRADO*****");
                print(local["properties"]["place"]);
                print("*****LUGAR ESPECIAL ENCONTRADO*****");
            else:
                print(local["properties"]["place"]);
            
ManiputaJSON();
        
        
        

