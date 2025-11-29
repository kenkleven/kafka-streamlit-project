import faust 

app = faust.App('filter-visits',broker='kafka://kafka:9092')

class Visit(faust.Record, serializer='json'):
    id: int
    nom: str
    duree: int
    date: str

visits_topic = app.topic("visits", value_type=Visit)
long_topic = app.topic("long_visits", value_type=Visit)

@app.agent(visits_topic)
async def process(visits):
    async for v in visits:
        if v.duree > 30:
            print("Visit > 30s:", v)
            await long_topic.send(value=v)

if __name__ == '__main__':
    app.main()
