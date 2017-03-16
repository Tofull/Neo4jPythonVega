from py2neo import Graph, authenticate
from pandas import DataFrame

# http://py2neo.org/v3/database.html#py2neo.database.Cursor

VERBOSE = True


def connect_to_db():
    authenticate("localhost:7474", "neo4j", "social")
    graph = Graph()
    return graph


def get_histogram_of_relation(g):
    query = "MATCH (n) RETURN n.name AS name, SIZE((n)-[:FACEBOOK]->()) AS FACEBOOK,SIZE((n)-[:GOOGLE]->()) AS GOOGLE,SIZE((n)-[:LINKEDIN]->()) AS LINKEDIN"
    cursor = g.run(query)
    df = DataFrame(cursor)
    # add columns with sum of relations per individual
    df['TOTAL'] = df['FACEBOOK']+df['GOOGLE']+df['LINKEDIN']
    cursor.close()
    '''
    # build json
    jsondata = '"data": ['+\
        +'{'+\
            +'"name": "table",'+\
            +'"values": ['+\
              +'  {"x": 0, "y": 28, "c": 0}, {"x": 0, "y": 55, "c": 1}, '+\
                  +'  {"x": 1, "y": 43, "c": 0}, {"x": 1, "y": 91, "c": 1},'+\
        +'                {"x": 2, "y": 81, "c": 0}, {"x": 2, "y": 53, "c": 1}, '+\
                  +'                {"x": 3, "y": 19, "c": 0}, {"x": 3, "y": 87, "c": 1},'+\
                +'{"x": 4, "y": 52, "c": 0}, {"x": 4, "y": 48, "c": 1}, '+\
                  +'{"x": 5, "y": 24, "c": 0}, {"x": 5, "y": 49, "c": 1},'+\
                +'{"x": 6, "y": 87, "c": 0}, {"x": 6, "y": 66, "c": 1}, '+\
                  +'{"x": 7, "y": 17, "c": 0}, {"x": 7, "y": 27, "c": 1},'+\
                +'{"x": 8, "y": 68, "c": 0}, {"x": 8, "y": 16, "c": 1}, '+\
                  +'{"x": 9, "y": 49, "c": 0}, {"x": 9, "y": 15, "c": 1}'+\
            +'] '+\
            +'},'+\
        +'{ '+\
        +'  "name": "stats",'+\
          +'  "source": "table",'+\
            +'"transform": ['+\
              +'  { '+\
                +'    "type": "aggregate",'+\
                  +'  "groupby": ["x"],'+\
                    +'"summarize": [{"field": "y", "ops": ["sum"]}]'+\
                +'} '+\
                  + ']'+\
        +'} '+\
          + ']'
    '''
    return df.to_json(orient='records')

#def get_no_of_persons_per_network(df) :


'''

if __name__ == "__main__":
    graph = connect_to_db()
    df = get_histogram_of_relation()

    print("\n---------\nThe end.")

'''