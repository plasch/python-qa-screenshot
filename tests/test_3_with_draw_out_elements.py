import time
import allure

from screenshots.helpers import comparison_test_light_with_draw, make_tmp_file


@allure.label("testType", "screenshotDiff")
@allure.title("Comparing pages test with draw elements out")
def test_main_page_draw_elements_out(browser):
    master_path = make_tmp_file(browser, "prod")
    staging_path = make_tmp_file(browser, "staging")
    diff_path = make_tmp_file(browser, "diff")

    browser.get(browser.prod_url)
    time.sleep(3)  # We want slider swipe
    # slider_dim = browser.find_element_by_css_selector("#slideshow0").rect
    # slider_pag_dim = browser.find_element_by_css_selector(".swiper-pagination").rect
    browser.save_screenshot(master_path)

    browser.get(browser.stag_url)
    browser.save_screenshot(staging_path)

    comparison_test_light_with_draw(
        master_path,
        staging_path,
        diff_path,
        # draw_out=[slider_dim, slider_pag_dim],
        clear_images=False
    )
