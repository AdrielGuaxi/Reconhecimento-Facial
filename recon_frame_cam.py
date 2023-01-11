import cv2
import face_recognition as fr
#Pegando a base de pessoas autorizadas para níves 1, 2 e 3
filesnv1 = ["imagema.jpeg"]
filesnv2 = ["imagemb.jpeg"]
filesnv3 = ["imagemc.jpeg", "imagemc2.jpeg"]
imagesnv1 = []
imagesnv2 = []
imagesnv3 = []
#Carregando imagens de pessoas autorizadas níves 1, 2 e 3
for file in filesnv1:
    imagesnv1.append(fr.load_image_file(file))
for file in filesnv2:
    imagesnv2.append(fr.load_image_file(file))
for file in filesnv3:
    imagesnv3.append(fr.load_image_file(file))
#Capturando imagem da pessoa que deseja acessar
cam = cv2.VideoCapture(0)
while cam.isOpened():
    verificador, frame = cam.read()
    if not verificador:
        break
    im = frame
    face_loc = fr.face_locations(im)
    if len(face_loc) > 0:
        cv2.rectangle(im, (face_loc[0][3], face_loc[0][0]), (face_loc[0][1], face_loc[0][2]),(0, 255, 0), 2)
    #cv2.putText(im,"Aperte s para tirar foto para autorizacao",(80, 20),cv2.QT_FONT_NORMAL,0.7,200)
    cv2.imshow("Camera", im)
    if cv2.waitKey(3) == ord('s'):
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        encode_im = fr.face_encodings(im)[0]
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        cam.release()
        cv2.destroyAllWindows()
        break
i = 0
#checando acesso ao nível 1
for imagenv1 in imagesnv1:
    imagenv1 = cv2.cvtColor(imagenv1, cv2.COLOR_BGR2RGB)
    encode_imagenv1 = fr.face_encodings(imagenv1)[0]
    validacao = fr.compare_faces([encode_im], encode_imagenv1)
    if validacao[0] == True:
        cv2.putText(im,"Autorizado para nivel 1",(50,20),cv2.QT_FONT_NORMAL,1,255)
        i += 1
        break
#Checando acesso ao nível 2
for imagenv2 in imagesnv2:
    imagenv2 = cv2.cvtColor(imagenv2, cv2.COLOR_BGR2RGB)
    encode_imagenv2 = fr.face_encodings(imagenv2)[0]
    validacao = fr.compare_faces([encode_im], encode_imagenv2)
    if validacao[0] == True:
        cv2.putText(im,"Autorizado para nivel 2",(50,20),cv2.QT_FONT_NORMAL,1,255)
        i += 1
        break
#Checando acesso ao nível 3
for imagenv3 in imagesnv3:
    imagenv3 = cv2.cvtColor(imagenv3, cv2.COLOR_BGR2RGB)
    encode_imagenv3 = fr.face_encodings(imagenv3)[0]
    validacao = fr.compare_faces([encode_im], encode_imagenv3)
    if validacao[0] == True:
        cv2.putText(im,"Autorizado para nivel 3",(50,20),cv2.QT_FONT_NORMAL,1,255)
        i += 1
        break
if i == 0:
    cv2.putText(im,"Sem Acesso",(50,20),cv2.QT_FONT_NORMAL,1,255)
#Mostrando na tela o nível de acesso que o usuário possuí, se não possuir nenhum, aparecerá sem acesso
cv2.imshow("Autorizacao", im)
cv2.waitKey(0)