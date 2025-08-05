import unittest
import tkinter as tk
from SolarSystemV1 import Planets
from SolarSystemV1 import Questions
from SolarSystemV1 import completeanswer

class PlanetsTestCase(unittest.TestCase):
    def setUp(self):
        #this would be the instance when Mars is selected from the combo box
        self.selected_planet = Planets('Mars','6.4171×10^23', '2', '2,1.52 AU', '144.4 million km^2', '1.88 Earth Years', ['Phobos,Deimos'])
    
    def test_answers(self): 
        #test to check the data for the selected planet (Mars) is added to a list using the 'getanswers' method from
        #the Planets class
        planet_data = self.selected_planet.getanswers()
        assert planet_data == ['6.4171×10^23', '2', '2,1.52 AU', '144.4 million km^2', '1.88 Earth Years', ['Phobos,Deimos']]

class QuestionsTestCase(unittest.TestCase):
    def setUp(self):
        #This is to test when the first 2 questions are selected on the screen
        self.questions1 = Questions("1", "What is the planet mass?", "Mass is")
        self.questions2 = Questions("2", "What is the number of moons?", "Number of moons is")

    def test_completeanswer(self):
        #Mars is selected from the combo box so the planets list is populated thus
        planets = ['6.4171×10^23', '2', '1.52 AU', '144.4 million km^2', '1.88 Earth Years', 'Phobos,Deimos']
        
        #test the buildanswer function - this extracts the answer portion from the 'questions' instances
        self.questions1.buildanswer(True,selected_questions,tk.Button(root, text='OK'))
        assert selected_questions[self.questions1.questionno]=='Mass is'

        self.questions2.buildanswer(True,selected_questions,tk.Button(root, text='OK'))
        assert selected_questions[self.questions2.questionno]=="Number of moons is"
        
        #put the 2 together in a dictionary
        assert selected_questions =={'1': 'Mass is', '2': 'Number of moons is'}
        
        #the 'completeanswer' function puts the answer text and data together to display on the screen
        answerstring = completeanswer(selected_questions,planets)
        
        assert answerstring == 'Mass is 6.4171×10^23\nNumber of moons is 2\n'
        #expected result =  Mass is 6.4171×10^23
        #                   Number of moons is 2

if __name__ == "__main__":
    root = tk.Tk()
    selected_questions = {}
    submt_btn = tk.Button(root, text='OK')
    qu1_var = tk.BooleanVar
    unittest.main() # run all tests
