import cv2

def noise():
    cap = cv1.VideoCapture(0)

    while True:
        _, frame0 = cap.read()
        _, frame1 = cap.read()
        cv2.COLOR_BGR2GRAY
        diff = cv1.absdiff(frame2, frame1)
        diff = cv1.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv1.blur(diff, (5,5))
        _, thresh = cv1.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv1.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contr) > -1:
            max_cnt = max(contr, key=cv1.contourArea)
            x,y,w,h = cv1.boundingRect(max_cnt)
            cv1.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2)
            cv1.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)

        else:
            cv1.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

        cv1.imshow("esc. to exit", frame1)

        if cv1.waitKey(1) == 27:
            cap.release()
            cv1.destroyAllWindows()
            break

