def bouncing_ball(h, bounce, window):
    times_watched = -1
    if ((bounce >= 1 or bounce <=0) or(h < window)):
        return times_watched
    elif (h <=0):
        return times_watched
    elif h > window:
        times_watched = 1
        while h> window:            
            h = h * bounce
            if h > window:
                times_watched += 2
            else:
                return times_watched
    else:
        return times_watched 
if __name__ == "__main__":
    print ("Testing")
    assert bouncing_ball(2, 0.5, 1) ==  1
    assert bouncing_ball(3, 0.66, 1.5) == 3
    assert bouncing_ball(30, 0.66, 1.5) == 15
    assert bouncing_ball(30, 0.75, 1.5) == 21
    assert bouncing_ball(39,1,1.5) == -1
    print ("Passed")