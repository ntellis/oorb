if __name__ == "__main__":
    
    import argparse
    import numpy as np
    import pyoorb as oo
    err = oo.pyoorb.oorb_init()
    ### version = '1.0.2.post480+475dc9d.dirty'
    
    parser = argparse.ArgumentParser(description='Crash PYOORB.')
    parser.add_argument('--single_epoch', action="store_true", help="Generate ephemerides at a single epoch first and then generate ephemerides at all epochs. Causes soft crash instead of a hard crash.")
    args = parser.parse_args()
​
    H = 21.0
    G = 0.15
    ORBIT_TIME_SCALE = 3
    ORBIT_TYPE = 1
​
    orbit = np.array([[
            0,
            +1.9060244971350251e+00,
            -1.3235019335069369e+00,
            -1.1200264141987071e+00,
            +3.4454193624532409e-03,
            +7.5416130381036756e-03, 
            -8.8697384865393607e-04,
            ORBIT_TYPE,
            56540.03663345522,       # epoch in MJD TT
            ORBIT_TIME_SCALE,
            H,
            G,
        ]],
        dtype=np.double,
        order="F"
    )
    epochs = np.array([
            [56539.26802978944, 1],
            [56539.26940018218, 1],
            [56539.27077569720, 1],
            [56540.04616529355, 1],
            [56545.14362057485, 1],
        ],  
        order="F"
    )
​
    # Case 1
    # Note: ephemeris generation at first epoch
    if args.single_epoch:
        print("Generating ephemerides at a single epoch...")
        ephemeris, err = oo.pyoorb.oorb_ephemeris_basic(
            in_orbits=orbit,
            in_obscode="I41",
            in_date_ephems=epochs[:1],
            in_dynmodel="N"
        )
        print(ephemeris)
        print(err)
​
    # Case 2
    # Note: ephemeris generation at all epochs
    print("Generating ephemerides at all epochs...")
    ephemeris, err = oo.pyoorb.oorb_ephemeris_basic(
        in_orbits=orbit,
        in_obscode="I41",
        in_date_ephems=epochs,
        in_dynmodel="N"
    )
    print(ephemeris)
    print(err)
