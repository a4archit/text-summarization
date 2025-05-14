# setup dependencies
from transformers import T5Tokenizer, T5ForConditionalGeneration
import tensorflow as tf


class TEXTT5:
    """ This class treat as module for project text summarization """


    def __init__(self):
        """ Constructor """

        # declaring variables
        self.min_length = 10
        self.max_length = 100
        
        # Load pretrained tokenizer and model
        self.tokenizer = T5Tokenizer.from_pretrained("t5-small")
        self.model = T5ForConditionalGeneration.from_pretrained("t5-small")


    def set_min_length(self, length: int) -> None :
        """ this function  will set the value of minimum summary length """
        self.min_length = length

    
    def set_max_length(self, length: int) -> None :
        """ this function  will set the value of maximum summary length """
        self.max_length = length


    def summarize_text(self, text: str, display: bool = False) -> str:
        """ this function will summarize given text using T5-small (pretrained model) and returns summarized text """

        # Add the "summarize:" prefix as T5 is task-based
        input_text = "summarize: " + text.strip()
        
        # Tokenize the input
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
        
        # Generate the summary
        output_ids = self.model.generate(
            input_ids,
            max_length = self.max_length,
            min_length = self.min_length,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
        )
        
        # Decode the output
        summary = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        if display:
            print(f"Summary: {summary}")
            
        return summary





if __name__ == "__main__":
    model = TEXTT5()
    model.summarize_text("hello my self archit tyagi", display=True)
