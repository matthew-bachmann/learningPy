from manim import *
import math

class SampleSpace(Scene):
    def construct(self):
        
        plane = NumberPlane()
        plane.add_coordinates()
        
        pop_size = 75 
        
        # create both circles and titles
        pop = Circle(radius=3,color=BLUE,fill_opacity=0.2)
        pop_title = Tex("Population").next_to(pop, UP)
        samp = Circle(radius=3*math.sqrt(.6),color=BLUE,fill_opacity=0.2).shift(RIGHT*3)
        samp_title = Tex("Sample").next_to(samp, UP)
        self.play(Create(pop))

        # generate dots that will become the sample
        r = np.array(np.sqrt(np.random.uniform(size=pop_size))*2.8)
        theta = np.array(np.random.uniform(size=pop_size)*2*math.pi)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        trigger = np.array(np.random.choice([-1,1],pop_size,p=[.3,.7]))
        

        population = VGroup()
        sample = VGroup()
        population.add(pop)
        
        
        for i in range(pop_size):
            p = Dot(radius =.06,color = RED).shift(RIGHT * (x[i]) + UP*y[i])
            population.add(p)
            if trigger[i] < 0:
                sample.add(p)
            self.play(FadeIn(p),run_time=.05)
        self.play(Write(pop_title))
        population.add(pop_title)
        self.play(population.animate.shift(LEFT*3))
        
        
        self.play(Create(samp))
        self.play(Indicate(sample,scale_factor=1.3),run_time=2)
        anims = []
        for p in sample.submobjects:
            x_dot = ((p.get_x() + 3) * (.6)) + 3
            y_dot = (p.get_y() * .6)
            anims.append(p.animate.move_to([x_dot,y_dot,0]))
        self.play(*anims)
        self.play(Write(samp_title))
            
        self.wait(4)
        