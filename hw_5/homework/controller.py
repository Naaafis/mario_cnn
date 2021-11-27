import pystk


def control(aim_point, current_vel):
    """
    Set the Action for the low-level controller
    :param aim_point: Aim point, in screen coordinate frame [-1..1]
    :param current_vel: Current velocity of the kart
    :return: a pystk.Action (set acceleration, brake, steer, drift)
    """
    action = pystk.Action()

    #action.acceleration = 1

    '''
    

    print(aim_point)
    print(current_vel)

    
    if aim_point[0] > -0.3 and aim_point[0] < 0.3 and current_vel < 18:
        action.steer = aim_point[0]
        action.nitro = True
        action.acceleration = 1
        
    elif aim_point[0] > -0.3 and aim_point[0] < 0.3 and current_vel > 18:
        action.steer = aim_point[0] 
        action.acceleration = 0.75
        action.nitro = True

    elif aim_point[0] > 0.2 and aim_point[0] < 0.50:
        action.drift = True
        action.steer = aim_point[0] + 0.5
        action.nitro = True
        action.acceleration = 0.75

    elif aim_point[0] < -0.2 and aim_point[0] > -0.50:
        action.drift = True
        action.steer = aim_point[0] - 0.5
        action.nitro = True
        action.acceleration = 0.75

    elif aim_point[0] > 0.50:
        action.drift = False
        action.steer = aim_point[0] + 0.5
        if current_vel < 15:
            action.acceleration = 0.95
        else:
            action.acceleration = 0.75
        

    elif aim_point[0] < -0.50:
        action.drift = False
        action.steer = aim_point[0] - 0.5
        if current_vel < 15:
            action.acceleration = 0.95
        else:
            action.acceleration = 0.75


    elif aim_point[0] == -1 or aim_point[0] == 1:
        action.drift = False
        action.brake = True
        if aim_point[0] == -1:
            action.steer = -1
        elif aim_point[0] == -1:
            action.steer = 1
        action.nitro = True
        acceleration = 0.6

    if aim_point[1] > 0.12 and aim_point[1] < 0.30:
        action.brake = True
        action.drift = True
        if aim_point[0] < 0:
            action.steer = aim_point[0] - 0.55
            action.acceleration = 0.75
        if aim_point[0] > 0:
            action.steer = aim_point[0] + 0.55
            action.acceleration = 0.75


    if aim_point[1] > 0.30 or aim_point[1] < -0.60:
        action.brake = True
        action.drift = False
        if aim_point[0] < 0:
            action.steer = aim_point[0] - 0.55
            action.acceleration = 0.75
        if aim_point[0] > 0:
            action.steer = aim_point[0] + 0.55
            action.acceleration = 0.75


    action.acceleration = 0.75
    print(aim_point)

    
    '''

    #some conditionals seemed to be ignored, possibly due to the fact that there are too many cases so here is a reduciton
    #also noone seems to be using the aim_points vertical dat

    if aim_point[0] > 0:
        action.steer = aim_point[0] + 0.75
    if aim_point[0] < 0:
        action.steer = aim_point[0] - 0.75

    if abs(aim_point[0]) > 0.2:
        action.drift = True
        if aim_point[0] > 0.5:
            action.drift = False
            action.steer = aim_point[0] + 0.5
        if aim_point[0] < -0.5:
            action.drift = False
            action.steer = aim_point[0] - 0.5
    else:
        action.drift = False

    if abs(aim_point[0]) < 0.30:
        action.nitro = True
        action.acceleration = 1

    else:
        action.acceleration = 0.75
    print(aim_point)
    
    

    

    """
    Your code here
    Hint: Use action.acceleration (0..1) to change the velocity. Try targeting a target_velocity (e.g. 20).
    Hint: Use action.brake to True/False to brake (optionally)
    Hint: Use action.steer to turn the kart towards the aim_point, clip the steer angle to -1..1
    Hint: You may want to use action.drift=True for wide turns (it will turn faster)
    """

   

    

    return action



if __name__ == '__main__':
    from utils import PyTux
    from argparse import ArgumentParser

    def test_controller(args):
        import numpy as np
        pytux = PyTux()
        for t in args.track:
            steps, how_far = pytux.rollout(t, control, max_frames=1000, verbose=args.verbose)
            print(steps, how_far)
        pytux.close()


    parser = ArgumentParser()
    parser.add_argument('track', nargs='+')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    test_controller(args)
