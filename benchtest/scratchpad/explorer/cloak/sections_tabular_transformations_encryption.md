# Encryption 

Encryption converts plaintext data into ciphertext using an algorithm, such as AES (Advanced Encryption Standard). AES is a widely adopted symmetric encryption algorithm known for its robust data security. It operates on fixed-size blocks of data and offers one key size: 256 bits (AES256). 

By applying AES encryption, sensitive information is transformed into an unreadable format, which can only be deciphered with the corresponding decryption key.

Unlike [hashing (pseudonymisation)](/sections/tabular/transformations/pseudonymisation.md), encrypted data is reversible. Encrypted data can be decrypted back to its original form using decryption keys. 

---
## Examples

| Original value | Transformed value         |
|----------------|---------------------------|
| T0581222F      | xyMRlFrHkoma0HkFUC6qDQ==  |
| F0005772O      | 71qhltuKJVz8BXf2EUTBmw==  |
| T7303748A      | 8O7kbq1LRJ1TDGg9zxGRjQ==  |
| T6353952U      | KsqNArQUnTXHzvKIVdSxjw==  |
| T0357152V      | +3OQKzms2JG2dMopPvgV3g==  |

--- 
## Usage Guide 

| Inputs         | Description                                                         |
|----------------|---------------------------------------------------------------------|
| Encryption Key | Secret Key and Initial Vector used by the AES encryption algorithm  |

---
## Helper Code 

If you would like to decrypt the ciphertext using AES256 encryption. Follow the provided helper codes to securely transform the ciphertext back into its original plaintext form. Safeguard the encryption key or passphrase for authorised access to decrypted data. You can find the secret key and initial vector used by the AES256 encryption algo under **Home Page -> Settings -> Secrets**.

![encryption-1](_resources/encryption-1.png)

*The Secrets page showing a stored encryption secret with its ID, key, and initialisation vector (IV).*

---

### Python 

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(ciphertext, key, IV):
    """
    Decrypts the ciphertext using the AES encryption algorithm with CBC mode.

    Args:
        ciphertext (str): The ciphertext to decrypt as a Base64-encoded string.
        key (str): The encryption key as bytes.
        IV (str): The initialization vector (IV) as bytes.

    Returns:
        str: The decrypted plaintext.

    """
    ciphertext = base64.b64decode(ciphertext.encode('utf-8'))
    cipher = AES.new(bytes(key, 'utf-8'), AES.MODE_CBC, bytes(IV, 'utf-8'))
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')
```
>  Make sure you have the `crypto` library installed in your project to use this code.

Here's an example that demonstrates how to call the `decrypt` method:
```python
key = 'SuperSecretKey123456789123456789'
ciphertext = 'xXYoVS1+LnQDP8Cj5cXkBdhtECXOPLuYDPedsCPTvg8='
IV = '0123456789ABCDEF'

plaintext = decrypt(ciphertext, key, IV)
print(plaintext)

# This is a secret message!
```
---

Here's an example that demonstrates how to apply the `decrypt` method on a dataframe:

encrypted_1 column is encrypted using following key and IV
```python
key = 'SuperSecretKey123456789123456789'
IV = '0123456789ABCDEF'
```

encrypted_2 column is encrypted using following key and IV
```python
key2 = 'SuperSecretKey987654321987654321'
IV2 = 'FEDCBA9876543210'
```

| raw_data                   | encrypted_1                                  |  encrypted_2                                 |
|----------------------------|----------------------------------------------|----------------------------------------------|
| Hello                      | FV0KJDltmW4/yMiCNpU9ug==                     | 5HZ29gHo0/nfPZaJkKWAgQ==                     |
| World                      | dWuglF+vrfEvFg79XB9opg==                     | Opylwo7EnM+gVxpGhNl6/w==                     |
| This is a secret message!  | xXYoVS1+LnQDP8Cj5cXkBdhtECXOPLuYDPedsCPTvg8= | aay/iCxdQoxphRbpqCr3VLd+zBWkptOWFdU42wC9I68= |

---

```python
import pandas as pd

data = {
    'raw_data': [
        'Hello',
        'World',
        'This is a secret message!'
    ],
    'encrypted_1': [
        'FV0KJDltmW4/yMiCNpU9ug==',
        'dWuglF+vrfEvFg79XB9opg==',
        'xXYoVS1+LnQDP8Cj5cXkBdhtECXOPLuYDPedsCPTvg8='
    ],
    'encrypted_2': [
        '5HZ29gHo0/nfPZaJkKWAgQ==',
        'Opylwo7EnM+gVxpGhNl6/w==',
        'aay/iCxdQoxphRbpqCr3VLd+zBWkptOWFdU42wC9I68='
    ]
}

df = pd.DataFrame(data)

# Apply key and IV on encrypted_1 column
df['decrypted_1'] = df['encrypted_1'].apply(decrypt, args=[key, IV])

# Apply key2 and IV2 on encrypted_1 column
df['decrypted_2'] = df['encrypted_2'].apply(decrypt, args=[key2, IV2])

print(df)
```
---

You should be able to see the output as below:

| raw_data              | encrypted_1                       | encrypted_2                       | decrypted_1            | decrypted_2            |
|-----------------------|-----------------------------------|-----------------------------------|------------------------|------------------------|
| Hello                 | FV0KJDltmW4/yMiCNpU9ug==          | 5HZ29gHo0/nfPZaJkKWAgQ==          | Hello                  | Hello                  |
| World                 | dWuglF+vrfEvFg79XB9opg==          | Opylwo7EnM+gVxpGhNl6/w==          | World                  | World                  |
| This is a secret message! | xXYoVS1+LnQDP8Cj5cXkBdhtECXOPLuYDPedsCPTvg8= | aay/iCxdQoxphRbpqCr3VLd+zBWkptOWFdU42wC9I68= | This is a secret message! | This is a secret message! |

---

### Nodejs

```javascript
const CryptoJS = require('crypto-js');

function decrypt(ciphertext, key, IV) {
  const keyBytes = CryptoJS.enc.Utf8.parse(key);
  const ciphertextBytes = CryptoJS.enc.Base64.parse(ciphertext);
  const IVBytes = CryptoJS.enc.Hex.parse(IV);

  const decrypted = CryptoJS.AES.decrypt(
    { ciphertext: ciphertextBytes },
    keyBytes,
    {
      iv: IVBytes,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7,
    }
  );

  return decrypted.toString(CryptoJS.enc.Utf8);
}
```
>Make sure you have the `crypto-js` library installed in your project to use this code.

---

### Java

```java
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;

public class Decryptor {
    public static String decrypt(String ciphertext, String key, String IV) throws Exception {
        byte[] keyBytes = key.getBytes("UTF-8");
        byte[] ciphertextBytes = Base64.getDecoder().decode(ciphertext);
        byte[] IVBytes = hexStringToByteArray(IV);

        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec secretKeySpec = new SecretKeySpec(keyBytes, "AES");
        IvParameterSpec ivParameterSpec = new IvParameterSpec(IVBytes);
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, ivParameterSpec);

        byte[] plaintextBytes = cipher.doFinal(ciphertextBytes);
        return new String(plaintextBytes, "UTF-8");
    }

    private static byte[] hexStringToByteArray(String hexString) {
        int length = hexString.length();
        byte[] byteArray = new byte[length / 2];
        for (int i = 0; i < length; i += 2) {
            byteArray[i / 2] = (byte) ((Character.digit(hexString.charAt(i), 16) << 4)
                    + Character.digit(hexString.charAt(i + 1), 16));
        }
        return byteArray;
    }
}
```
>Please note that in the code above, the `decrypt` method throws an `Exception` which you can handle accordingly in your application. Also, ensure that you have the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files installed to support AES-256 encryption

?> Need help? Try our [Support Assistant](https://go.gov.sg/cloak-support-assistant) or visit the [Support page](/sections/support.md).
