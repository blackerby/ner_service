import spacy
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="NER service based on spaCy",
    description="""
Provides the NER component from [spaCy](https://spacy.io/) as web service.
 - spaCy: 3.5.2
 - Model: [en_core_web_sm](https://spacy.io/models/en#en_core_web_sm)
""",
    docs_url="/",
)


# load trained pipeline with only the NER component
nlp = spacy.load(
    "en_core_web_sm",
    disable=[
        "tok2vec",
        "tagger",
        "morphologizer",
        "parser",
        "attribute_ruler",
        "lemmatizer",
    ],
)


class NER_Request(BaseModel):
    """
    Request with text to perform NER.
    """

    text: str = Field(
        ...,
        title="Text",
        description="Text to extract entities from.",
        example="Alabama Jazz Hall of Fame",
    )


class Entity(BaseModel):
    """
    Named Entity found in the text.
    """

    start: int = Field(
        ...,
        title="Start",
        description="Start position of entity in the text.",
        ge=0,
        example=0,
    )
    end: int = Field(
        ...,
        title="End",
        description="End position of entity in the text.",
        ge=1,
        example=2,
    )
    text: str = Field(
        ...,
        title="Text",
        description="The text of the Named Entity.",
        min_length=1,
        example="Martin Luther",
    )
    label: str = Field(
        ...,
        title="Label",
        description="The label (type) for the Named Entity.",
        example="PER",
    )


@app.post(
    "/ner",
    response_model=list[Entity],
    summary="Perform NER on text.",
    response_description="List of found entities.",
)
def ner(ner_request: NER_Request):
    """
    Performs a Named Entity Recognition on the given `text`.
    Will return the found entities in a list.
    """
    doc = nlp(ner_request.text)
    return [
        Entity(start=ent.start, end=ent.end, text=ent.text, label=ent.label_)
        for ent in doc.ents
    ]
