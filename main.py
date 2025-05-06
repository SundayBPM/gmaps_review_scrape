from scraper import GoogleMapsScraper

if __name__ == '__main__':
    with GoogleMapsScraper(debug=False) as scraper:
        url = 'https://www.google.com/maps/place/Warung+Sate+Shinta/@-6.9271091,107.5978321,17z/data=!3m1!4b1!4m8!3m7!1s0x2e68e679d2b2d00f:0xb3b66e1d30ed02a7!8m2!3d-6.9271091!4d107.600407!9m1!1b1!16s%2Fg%2F11r_3dn6vq?entry=ttu'
        scraper.driver.get(url)
        reviews = scraper.get_reviews(offset=0)
        
        # simpan ke csv
        import pandas as pd
        df = pd.DataFrame(reviews)
        df.to_csv('google_reviews.csv', index=False)
