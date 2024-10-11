from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    POSITIVE_SCORE: int
    NEGATIVE_SCORE: int
    POLARITY_SCORE: float
    SUBJECTIVITY_SCORE: float
    AVG_SENTENCE_LENGTH: float
    PERCENTAGE_OF_COMPLEX_WORDS: float
    FOG_INDEX: float
    WORD_COUNT: int
    SYLLABLE_PER_WORD: float
    PERSONAL_PRONOUNS: int
    AVG_WORD_LENGTH: float
