# Docker

Om de Docker-container uit te voeren, gebruik de volgende opdracht: \
```
docker run -it
    -v <pad/naar/lokale/afbeeldingen>:/app/afbeeldingen
    -v <pad/naar/lokale/output>:/app/output
    containernaam:versie
    <pad/van/afbeelding/om/te/verwerken>
```

*<pad/naar/lokale/output>* en *<pad/naar/lokale/afbeeldingen>* verwijzen naar de containermappen /app/output en /app/afbeeldingen, respectievelijk. \
*<pad/van/afbeelding/om/te/verwerken>* is het relatieve pad van de afbeelding die moet worden verwerkt op de container, beginnend vanaf /app/afbeeldingen.

# Clustering

## Verminder irrelevante kenmerken
Om de foto's zo goed mogelijk te clusteren is het aangeraden om zo weinig mogelijk irrelevante informatie over te houden, zodat het algoritme optimaal werkt. De volgende technieken zijn voorbeelden van manieren om dit aan te pakken.

### Cropping
In de voorbeeldfoto's bestaat een groot deel van de foto uit de achtergrond. Deze is niet relevant voor het detecteren van deffecgten op de capsule, dus deze wordt best verwijdert.
Vb. \
![Originele afbeelding](images\Screenshot_2023-10-28_at_14.32.45.png)
![gecropte afbeelding](images\crop_1.png)

Dit kan bekomen worden door een bounding box te maken met behulp van een threshold.
```py
def crop_img(img):
    #grayscale
    image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #threshold
    threshold = 150
    thresh_mask = image_grey < threshold
    image_grey[thresh_mask] = 255
    image_grey[~thresh_mask] = 0
    # crop using bounding box of thresholded image
    rows = np.any(thresh, axis=1)
    cols = np.any(thresh, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    return img[rmin:rmax, cmin:cmax]

```

Indien men enkel defecten verwacht in het rode gedeelte kan men ook het zwarte gedeelte verwijderen.

### kleurpallet verminderen
De originele foto's bevatten veel detail dat niet nodig is voor de clustering.
Door het totaal aantal kleuren in de foto te verminderen kan men de data minder complex maken. Dit kan clustering eenvoudiger en correcter maken.

Vb. Kmeans clustering (6 kleuren) \
![originele gecropte afbeelding](images\crop_1.png)
![reduced gecropte afbeelding](images\reduced_1.png)

De foto met het gereduceerde kleurenpalet heeft nu minder detail, maar het defect is nog steeds zeer goed zichtbaar. Het aantal kleuren kan worden aangepast als er meer of minder kleurendetail nodig is.

### PCA

Principle Component Analysis (PCA) kan worden gebruikt om het aantal eigenschappen van de foto's nog verder te verminderen. PCA zoekt de belangrijkste features in de foto's op basis van een vooraf bepaald aantal features, of een vooraf bepaald percentage dat aangeeft hoeveel data "verloren" mag gaan tijdens het verminderen van de features.

## Clusters vinden

Om de afbeeldingen te clusteren, kan men gebruik maken van diverse clustering algoritmes. Het beste algoritme hangt af van de verdeling van de data, en wordt dus best bepaald door middel van testen op de data.

Het juiste aantal clusters kan worden bepaald aan de hand van de "elbow"-methode waarbij men een aantal waarden kiest voor het aantal clusters en op de data uittest welke waarde de afstand tussen de clusters het beste verkleint voor het aantal clusters.