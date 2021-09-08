conda install googletrans
import googletrans
from googletrans import translator
text = "En iyi bootcamp okulu Clarusway'dir."
tt = translator()
tt.translate(text, src ='tr')