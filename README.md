# B2B Phone Sales

## Açıklama
B2B Phone Sales, işletmeler arası (B2B) telefon satışlarını yönetmek için geliştirilmiş bir Odoo modülüdür.  
Modülün sunduğu özellikler:

- Ürün Kategorileri Yönetimi
- Ürün Yönetimi
- Müşteri Yönetimi
- Sipariş Yönetimi
- Ödeme Takibi
- Erişim kontrolü: B2B User ve B2B Manager grupları ile

## Kurulum (Docker ile)

1. Modül klasörünü Docker Odoo container'ındaki `addons` dizinine kopyalayın:
   ```bash
   docker cp b2b_phone_sales adoo_proje-odoo-1:/mnt/extra-addons/

2.Odoo servisini yeniden başlatın:
docker restart adoo_proje-odoo-1

3.Odoo arayüzünden modülü yükleyin:

Uygulamalar (Apps) menüsüne gidin

B2B Phone Sales modülünü aratın

Yükle (Install) butonuna tıklayın

Modül güncellemesi yapmanız gerekiyorsa:
docker exec -it adoo_proje-odoo-1 odoo -d odoo -u b2b_phone_sales

Kullanım

Ürün Kategorileri: Master Data → Categories

Ürünler: Master Data → Products

Müşteriler: Master Data → Customers

Siparişler: Transactions → Orders

Ödemeler: Transactions → Payments

Raporlar: Reports → [B2B raporları]
Güvenlik

B2B User: Kendi oluşturduğu kayıtları görebilir, oluşturabilir ve düzenleyebilir.

B2B Manager: Tüm kayıtları görüntüleyebilir, oluşturabilir, düzenleyebilir ve silebilir.

Bağımlılıklar

base

sale

mail

Versiyon

Şu anki sürüm: 1.2

Lisans

LGPL-3


