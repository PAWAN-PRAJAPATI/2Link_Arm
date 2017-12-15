from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import ik_2link



class SimpleRobotArm:

    def __init__(self):
        self.name= "Simple Robot Arm"
        self.shoulder = 0
        self.elbow = 0
        self.arm = 0.0
        self.wrist = 0.0
        self.shoulder1=0


    def run(self):

        glutInit(sys.argv) # initialise the system
        # Configure inital display mode
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

        # Set up and display initial window
        glutInitWindowSize(1000,1000)
        glutInitWindowPosition(100,100)
        glutCreateWindow(self.name)  # See the __init__ method for self.name

        # Initial colour and shading model
        glClearColor(0.0,0.0,0.0,0.0)
        glShadeModel(GL_FLAT)

        # Register callback methods. The arguments are the names of
        # methods defined below.
        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        # glutMouseFunc(self.mouse) # not needed here
        glutKeyboardFunc(self.keys)
        
        glutMainLoop()
        
        # Launch the OGL event processing loop
        

    def display(self):
        glClear (GL_COLOR_BUFFER_BIT);
        glPushMatrix();

        glTranslatef (0, -0.6, -8);
        glRotatef (self.shoulder, 0, 1, 0);
        glTranslatef (0, 0.0, 0.0);
        glPushMatrix();
        glScalef (1, 1, 1);
        glutWireCube (0.5);
        glPopMatrix();

        glTranslatef(0, 0.25, 0);
        glRotatef(self.shoulder1, 0, 0.0, 1);
        glTranslatef(1.2, 0, 0.0);
        glPushMatrix();
        glScalef(2.0, 0.2, 0.5);
        glutWireCube(1.2);
        glPopMatrix();

        glTranslatef (1.2, 0.0, 0.0);
        glRotatef (self.elbow, 0.0, 0.0, 1.0);
        glTranslatef (1, 0.0, 0.0);
        glPushMatrix();
        glScalef (2.0, 0.2, 0.5);
        glutWireCube (1);
        glPopMatrix();

        glTranslatef (0.6, 0.0, 0.0);
        glRotatef (self.wrist, 1, 0, 0);
        glTranslatef (0.5, 0.0, 0.0);
        glPushMatrix();
        glScalef (0.6, 0.7, 0.8);
        glutWireCube (0.5);
        glPopMatrix();
        


        
        
        glPopMatrix();
        glutSwapBuffers();

    def reshape(self,w,h):
        glViewport (0, 0, w, h)
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, w/h, 1.0, 20.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef (0.0, 0.0, -6.0)

    def keys(self,*args):
        key = args[0]
        
        if (key == 'a'.encode("utf-8")):
            self.shoulder = (self.shoulder+5) % 360
        elif (key==('d').encode("utf-8")):
            self.shoulder = (self.shoulder-5) % 360
        elif (key==('e').encode("utf-8")):
            self.elbow = (self.elbow+5) % 360
        elif (key==('E').encode("utf-8")):
            self.elbow = (self.elbow-5) % 360
        elif (key==('w').encode("utf-8")):
            self.arm = (self.arm+5) % 360
        elif (key==('W').encode("utf-8")):
            self.arm = (self.arm-5) % 360
        elif (key==('x').encode("utf-8")):
            self.wrist = (self.wrist-5) % 360
        elif (key==('X').encode("utf-8")):
            self.wrist = (self.wrist+5) % 360
        elif (key==('a').encode("utf-8")):
            self.finger2 = (self.finger2-5) % 360
      
        elif(key==('s').encode("utf-8")):
            self.shoulder1 = (self.shoulder1 + 5) % 360
        elif(key==('S').encode("utf-8")):
            self.shoulder1 = (self.shoulder1 - 5) % 360
        elif(key==('c').encode("utf-8")):
             angles=ik_2link.get_angles()
             print(angles)
             self.shoulder=(angles[1]*180)/3.14
             self.shoulder1=(angles[2]*180)/3.14
             self.elbow=(angles[3]*180)/3.14
             self.arm=(angles[4]*180)/3.14
            
        print("Base:",self.shoulder,"soulder:",self.shoulder1,"Elbow:",self.elbow,"Arm:",self.arm,"wrist:",self.wrist)
        glutPostRedisplay()


if __name__ == '__main__':
  app = SimpleRobotArm()
  app.run()
  



