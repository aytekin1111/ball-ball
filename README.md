# ball-ball
dont allow the white ball fall down
# Turkce
beyaz topu dusurme
# Ball Game - Python Version

🎮 beyaz topu dusurme
Python ve pygame kullanılarak geliştirilmiş eğlenceli bir refleks oyunu. Orijinal C++ OpenGL kodundan Python'a çevrilmiştir.

## 🎯 Oyun Kuralları
- **🖤 Siyah Toplar**: Mouse ile üzerlerinden geçerek yok edin (+10 puan)
- **🤍 Beyaz Toplar**: Alta ulaşırlarsa oyun biter!
- **⚡ Zorluk**: Zaman geçtikçe toplar daha hızlı düşer
- **🏆 Hedef**: Mümkün olduğunca yüksek puan yapın

## 🎮 Kontroller
| Kontrol                  | Açıklama                                   |
|--------------------------|--------------------------------------------|
| **Mouse Click + Drag**   | Siyah topları yok et                       |
| **R**                    | Oyunu yeniden başlat (Game Over durumunda) |
| **ESC / X**              | Oyundan çık                                |

## 🚀 Kurulum ve Çalıştırma
### Gereksinimler
- Python 3.7+
- pygame

### Kurulum
```bash
# Repository'yi klonlayın
git clone https://github.com/KULLANICI_ADIN/ball-game-python.git
cd ball-game-python

# Gerekli kütüphaneyi yükleyin
pip install pygame

# Oyunu çalıştırın
python ball_game.py
```

### Alternatif Kurulum
```bash
# Sadece dosyayı indirin
wget https://raw.githubusercontent.com/KULLANICI_ADIN/ball-game-python/main/ball_game.py

# pygame'i yükleyin
pip install pygame

# Oyunu başlatın
python ball_game.py
```

## 🎨 Oyun Özellikleri

### ✅ Mevcut Özellikler
- Pürüzsüz 60 FPS oynanış
- Dinamik zorluk sistemi
- Skor takibi
- Fade-out animasyonları
- Çarpışma tespiti
- Yeniden başlatma özelliği

### 🔮 Gelecek Özellikler
- [ ] Ses efektleri
- [ ] Parçacık sistemleri
- [ ] Power-up'lar (yavaşlatma, kalkan)
- [ ] Farklı oyun modları
- [ ] High score tablosu
- [ ] Ayarlar menüsü
- [ ] Mobil dokunmatik destek

## 🛠️ Teknik Detaylar

### Kod Yapısı
```
ball_game.py
├── Ball Class          # Top objesi ve davranışları
├── BallGame Class      # Ana oyun döngüsü
├── Event Handling      # Mouse/klavye kontrolü
└── Render System       # Çizim ve animasyonlar
```

### Performans
- **RAM Kullanımı**: ~20MB
- **CPU Kullanımı**: Düşük (single-threaded)
- **Uyumluluk**: Windows, macOS, Linux

## 🔄 C++ → Python Çevirisi
Bu proje, orijinal C++ OpenGL kodundan Python pygame'e çevrilmiştir:

| C++ Versiyonu | Python Versiyonu |
|---------------|-------------------|
| OpenGL ES | pygame |
| Manual memory management | Automatic garbage collection |
| Complex shaders | Simple drawing functions |
| Platform specific | Cross-platform |
| ~300 lines complex code | ~250 lines readable code |

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! 

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

### Katkı Alanları
- 🐛 Bug düzeltmeleri
- ✨ Yeni özellikler
- 📝 Dokümantasyon iyileştirmeleri
- 🎨 Grafik/UI geliştirmeleri
- 🔊 Ses efektleri
- 📱 Mobil uyumluluk

## 👨‍💻 Geliştirici

**bayrinat**

forked by:
**aytekin1111** - İnşaat Mühendisi & Python Developer

- GitHub: aytekin1111(https://github.com/aytekin1111)
- LinkedIn: https://www.linkedin.com/in/aytekin-naki-cikdi-b185bb17

## 🙏 Teşekkürler

- Orijinal C++ kodu için ilham veren proje: forked from **bayrinat/ndkGame**
- pygame topluluğu
- Python developer community


# English
# Ball Game - Python Version

🎮 **Don't Drop the White Ball**
A fun reflex game developed using Python and pygame. Converted from original C++ OpenGL code to Python.

## 🎯 Game Rules
- **🖤 Black Balls**: Click and drag across them to destroy (+10 points)
- **🤍 White Balls**: Game over if they reach the bottom!
- **⚡ Difficulty**: Balls fall faster as time progresses
- **🏆 Objective**: Achieve the highest score possible

## 🎮 Controls
| Control | Description |
|---------|-------------|
| **Mouse Click + Drag** | Destroy black balls |
| **R** | Restart game (when Game Over) |
| **ESC / X** | Exit game |

## 🚀 Installation and Running

### Requirements
- Python 3.7+
- pygame

### Installation
```bash
# Clone the repository
git clone https://github.com/aytekin1111/ball-game-python.git
cd ball-game-python

# Install required library
pip install pygame

# Run the game
python ball_game.py
```

### Alternative Installation
```bash
# Download file only
wget https://raw.githubusercontent.com/aytekin1111/ball-game-python/main/ball_game.py

# Install pygame
pip install pygame

# Start the game
python ball_game.py
```

## 🎨 Game Features
### ✅ Current Features
- Smooth 60 FPS gameplay
- Dynamic difficulty system
- Score tracking
- Fade-out animations
- Collision detection
- Restart functionality

### 🔮 Future Features
- [ ] Sound effects
- [ ] Particle systems
- [ ] Power-ups (slow motion, shield)
- [ ] Different game modes
- [ ] High score table
- [ ] Settings menu
- [ ] Mobile touch support

## 🛠️ Technical Details
### Code Structure
```
ball_game.py
├── Ball Class          # Ball object and behaviors
├── BallGame Class      # Main game loop
├── Event Handling      # Mouse/keyboard controls
└── Render System       # Drawing and animations
```

### Performance
- **RAM Usage**: ~20MB
- **CPU Usage**: Low (single-threaded)
- **Compatibility**: Windows, macOS, Linux

## 🔄 C++ → Python Conversion

This project has been converted from original C++ OpenGL code to Python pygame:

| C++ Version | Python Version |
|-------------|----------------|
| OpenGL ES | pygame |
| Manual memory management | Automatic garbage collection |
| Complex shaders | Simple drawing functions |
| Platform specific | Cross-platform |
| ~300 lines complex code | ~250 lines readable code |

## 🤝 Contributing

We welcome your contributions!

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Areas
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 Graphics/UI enhancements
- 🔊 Sound effects
- 📱 Mobile compatibility

## 👨‍💻 Developer

**bayrinat**

forked by:
**aytekin1111** - İnşaat Mühendisi & Python Developer

- GitHub: aytekin1111(https://github.com/aytekin1111)
- LinkedIn: https://www.linkedin.com/in/aytekin-naki-cikdi-b185bb17

## 🙏 Acknowledgments

- Original C++ code inspiration: forked from **bayrinat/ndkGame**
- pygame community
- Python developer community
