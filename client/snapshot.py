import requests
import cv2
import pickle
import crypt

r = requests.get('https://localhost:12344/snapshot-raw', verify="server.crt")
encryptedContent = pickle.loads(r.text)
frameString = crypt.Decrypt(encryptedContent[0], encryptedContent[1], encryptedContent[2])
img = pickle.loads(frameString)

cv2.imshow("Snapshot", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
