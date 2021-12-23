# Caesar Cipher

</h2><b>Introduction:</b></h2></br>
Supposedly named after the Roman Emperor Julius Caesar who had used this method of encryption to protect vital military commuication, the Caesar Cipher is one of the earliest and most simplest form of encryption. The Caesar Cipher is a subtitution cipher that works by replacing each letter from a given text by a letter some fixed number of positions down the alphabet. For example, a shift of 6 would mean that G would be replaced by A, H would be replaced by B and so on.

</br></br>
</h2><b>Research:</b></h2></br>
As I was my knowledge with encryption and ciphers are very limited, I did a simple Google search to get an understanding as to how the Caesar Cipher works in laymans terms so I looked up the Wikipedia entry as well as any other sites that would give a clear explanation as to how it works. Through these searches, I came across a site called dCode which has an online Caesar Cipher which I used to run multiple times to see how it runs and how to be able to apply this to my own program including doing a brute force decryption.


</br></br>
</h2><b>Program Overview:</b></h2></br>
When running this program for the first time, the user will be given a menu with 4 options and the user will then have to enter a number from 1 to 4 to select the option they want:

</br>
<li>Entering 1 will open the Encrypt option. This allows the user to enter the text they wish to encrypt and they will they be further asked to enter a number from 1 to 25 to signify the amount the letters will shift by. The program will then perform the shift of the user's input and displays the result on the screen.</li>
<li>Entering 2 will open the Decrypt option. This allows the user to enter the text they wish to decrypt, assuming they know both the encrypted text and the correct number of shifts which will display the original text before it was encrypted.</li>
<li>Entering 3 will open the Brute Force Decrypt option. This allows the user to enter the text they wish to decrypt but do not know the number of shifts to correctly decipher it. Because of this, the user is not asked to enter a number to shift by and the end result will display a list of all possible shifts for the text from 1 to 25</li>

</br></br>
</h2><b>References:</b></h2></br>
<a href ="https://www.dcode.fr/caesar-cipher">dCode</a> - Used this as a reference to compare with my program to ensure the cipher was correctly givng back the correct text.
