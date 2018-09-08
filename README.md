# ![AmazonScraper](https://s33.postimg.cc/omsthlxkv/amazon.png) Amazon Scraper

## Usage

```python
from amazonscraper import AmazonScraper
data = AmazonScraper.scrape('B003F2X13I')
print(data)
```

```json
{
  "asin": "B003F2X13I",
  "title": "Yamaha YPG-535 88-Key Portable Grand Piano with Stand and Power Adapter",
  "editorial_review": "YPG-535 features 88 Graded Soft Touch keyboard. All the best sounds are available at the push of button and recording virtuoso performances is simple with built-in recorder. The Yamaha Education Suite and USB connectivity (USB to Device) add functionality. Main features include USB MIDI, USB storage capability and high resolution Live! Grand stereo sample.",
  "features": [
    "88 piano-style keys with Graded Soft Touch. Includes stand, adapter, and sustain peda",
    "USB To Device: connect USB storage devices (storage device optional)",
    "Large Wave ROM features extra high quality Live! Grand sample", 
    "Backlit LCD (320 x 240) displays lyrics, chords & notatio",
    "Performance Assistant Technology features Melody Mode in addition to Chord and Chord/Free Model"
  ],
  "brand": "Yamaha", 
  "large_img_url": "https://images-na.ssl-images-amazon.com/images/I/71npKLfpgUL.jpg",
  "medium_img_url": "https://images-na.ssl-images-amazon.com/images/I/71npKLfpgUL._SL160_.jpg",
  "small_img_url": "https://images-na.ssl-images-amazon.com/images/I/71npKLfpgUL._SL75_.jpg",
  "list_price": "760.00",
  "price": "499.99"
}
```
