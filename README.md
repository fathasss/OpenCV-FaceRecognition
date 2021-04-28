# OpenCV-FaceRecognition
OpenCV and deepFace with FaceRecognition

Visual Studio Code ile yapıldı.✔<br>

OpenCV-FaceDetection uygulamasının gelişmiş hali. Buradan göz gezdirebilirsin: https://github.com/fathasss/OpenCV-FaceDetection<br>
Fotoğraflardaki yüzleri algılar ve iki fotoğraf arasında kıyaslama yapar.<br>
DeepFace kütüphanesinin çalışabilmesi için vgg_face_weights.h5 modelinin yüklenmesi gerekmektedir.<br>
Buradan yüklenebilir: https://drive.google.com/uc?id=1CPSeum3HpopfomUEK1gybeuIVoeJT_Eo

## Proje hedefi
1.Tensorflow kullanılarak bir model oluşturup model tanımlı yüzleri yapay zeka ile tanıma.<br>
2.TensorBoard ile modelin eğitim grafiklerinin görünmesi.

```
pip install opencv-python
pip install deepface
pip install matplotlib
```

#### Uygulama Çıktısı

![ekran](https://user-images.githubusercontent.com/32196738/116397329-2570a280-a82f-11eb-8adc-26200854fee1.PNG)

- [x] Opencv use
- [x] Matplotlib use
- [x] DeepFace use
- [ ] Tensorflow use

`dface = DeepFace.verify(path1,path2)` <br>
`print(dface)` <br>

`{'verified': True, 'distance': 0.2926552891731262, 'max_threshold_to_verify': 0.4, 'model': 'VGG-Face', 'similarity_metric': 'cosine'}`

- [x] `verified: True` Yüzlerin aynı olduğunu belirtir.
