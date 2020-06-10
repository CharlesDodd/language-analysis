# language-analysis
A quick experiment in the 'repetitiveness' of a language. Inspired by https://inventwithpython.com/cracking/ and their implimentation of the Kasiski method.

Kasiski examination is a method used to crack the Vigenère cipher by looking for repetivive character sequences. For example, in English short words such as 'and' appear frequently, so do other three character squences like ' I '. There is more than one way to get around this vulnerability :
  Use a one time pad.
  Change the plaintext to be less repetitious.
  **Use a different language?**

Perhaps you could translate your plaintext (with google or otherwise) into a language with a different structure? Are there languages whose default repetitiveness is more forgiving than English? **_How would you measure that?_**

In order to compare languages we would need _large, representitive, parallel_ texts. While the Bible has been translated into every language and is big enough, it might not be relevent to messages we're sending today. The Harry Potter collection might be better, but I couldn't find free text files for that in multiple languages. Using http://www.russianlessons.net/articles/index.php and websites like it, we can find enough parallel texts that when concatenated together, we could perhaps find a representative sample. (Alternatively, you could translate the plaintext into a variety of languages each time one sends a message - a general best fit language might be more interesting though!)

Next we could find the _most repetitive sequences_, and see _how repetitive they are_ compared to the english.

This script should help with that, as well as plotting the graph for the sequences.
