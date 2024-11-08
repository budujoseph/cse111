import pytest
from pytest import approx 
from shapes_calculator import circle_area, circle_circumference, rectangle_area, rectangle_perimter, sphere_volume, sphere_surface_area, surface_area_of_cone, cone_volume


def test_cirlce_area():
    """
    Verify that the circle_area function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the circle_area function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert circle_area(0) == approx(0, abs=0.001)
    assert circle_area(4.33) == approx(58.901, abs=0.001)
    assert circle_area(2.45) == approx(18.857, abs=0.001)
    assert circle_area(5.5) == approx(95.033, abs=0.001)
    assert circle_area(19) == approx(1134.115, abs=0.001)

def test_circle_circumference():
    """
    Verify that the circle_circumference function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the circle_circumference function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert circle_circumference(0) == approx(0)
    assert circle_circumference(2.45) == approx(15.394, abs=0.01)
    assert circle_circumference(5) == approx(31.416, abs=0.01)
    assert circle_circumference(20.2) == approx(126.920, abs=0.01)
    assert circle_circumference(122.4) == approx(769.062, abs=0.01)
    
def test_rectangle_area():
    """
    Verify that the rectangle_area function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the rectangle_area function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert rectangle_area(3,0) == approx(0, abs=0.1)
    assert rectangle_area(2.3, 5.8) == approx(13.34, abs=0.1)
    assert rectangle_area(8, 3.2) == approx(25.6, abs=0.1)
    assert rectangle_area(12.99, 34) == approx(441.66, abs=0.1)
    assert rectangle_area(134, 98.25) == approx(13165.5, abs=0.01)

def test_rectangle_perimeter():
    """
    Verify that the rectangle_perimeter function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the rectangle_perimeter function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert rectangle_perimter(7, 0) == approx(14)
    assert rectangle_perimter(9.22, 8.56) == approx(35.56)
    assert rectangle_perimter(121.567, 45.22) == approx(333.574)
    assert rectangle_perimter(1238, 12.4) == approx(2500.8)
    assert rectangle_perimter(2.61, 0.52) == approx(6.26)
    assert rectangle_perimter(25.2, 13.44) == approx(77.28)

def test_sphere_volume():
    """
    Verify that the sphere_volume function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the sphere_volume function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert sphere_volume(5.5) == approx(696.91, abs=0.01)
    assert sphere_volume(7.53) == approx(1788.44, abs=0.01)
    assert sphere_volume(67.4) == approx(1282532.26, abs=0.01)
    assert sphere_volume(15.6) == approx(15902.39, abs=0.01)
    assert sphere_volume(9.33) == approx(3401.99, abs=0.01)

def test_sphere_surface_area():
    """
    Verify that the sphere_surface_area function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the sphere_surface_area function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert sphere_surface_area(12) == approx(1809.557, abs=0.01)
    assert sphere_surface_area(13.25) == approx(2206.184, abs=0.01)
    assert sphere_surface_area(7) == approx(615.752, abs=0.01)
    assert sphere_surface_area(31.22) == approx(12248.296, abs=0.01)
    assert sphere_surface_area(13.24) == approx(2202.855, abs=0.01)

def test_cone_volume():
    """
    Verify that the cone_volume function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the cone_volume function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert cone_volume(8, 5) == approx(335.103, abs=0.001)
    assert cone_volume(7.5, 10) == approx(589.049, abs=0.001)
    assert cone_volume(18.32, 15) == approx(5271.944, abs=0.001)
    assert cone_volume(56.3, 21.5) == approx(71364.770, abs=0.001)
    assert cone_volume(114.23, 90.56) == approx(1237443.519, abs=0.001)

def test_surface_area_of_cone():
    """
    Verify that the surface_area_of_cone function works correctly, which calculates the area of the circle
    Parameter: none
    return: nothing
    """
    # Call the surface_area_of_cone function five times and use an assert
    # statement to verify that the area returned is correct each time
    assert surface_area_of_cone(5, 9) == approx(219.911, abs=0.001)
    assert surface_area_of_cone(7.2, 9) == approx(366.435, abs=0.001)
    assert surface_area_of_cone(12.52, 9.22) == approx(855.094, abs=0.001)
    assert surface_area_of_cone(56.3, 27.32) == approx(14790.009, abs=0.001)
    assert surface_area_of_cone(420, 950.6) == approx(1808464.094, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

