import cv2
import mediapipe as mp
import time
import pyautogui
cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
screen_width, screen_height = pyautogui.size()
mpDraw = mp.solutions.drawing_utils  
pTime=0
cTime=0
index_y = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id , lm in enumerate(handLms.landmark):      
                # print(id,lm)
                h,w,c= img.shape
                cx,cy = int(lm.x*w),int(lm.y*h) 
                # print(id,cx,cy)
                if id==8:
                    cv2.circle(img , (cx,cy),15, (255,0,255),cv2.FILLED)
                    index_x = screen_width/w*cx
                    index_y = screen_height/h*cy
                    pyautogui.moveTo(index_x,index_y)
                if id==4:
                    cv2.circle(img , (cx,cy),15, (255,0,255),cv2.FILLED)
                    index_x = screen_width/w*cx
                    thumb_y = screen_height/h*cy
                    print('outsid',abs(index_y - thumb_y))
                    if abs(index_y - thumb_y)<30:
                        pyautogui.click()
                        pyautogui.sleep(0.5)
            mpDraw.draw_landmarks(img  , handLms, mpHands.HAND_CONNECTIONS) 
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime= cTime    
    cv2.putText(img,str(int(fps)), (10,70) , cv2.FONT_HERSHEY_COMPLEX ,3 ,
                (255,0,255), 3 )  
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
