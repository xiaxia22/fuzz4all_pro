# Interface ContentSignerParameters

**Source:** `jdk.jartool\com\sun\jarsigner\ContentSignerParameters.html`

### Class Description

```java
@Deprecated
(
since
="9")
public interface
ContentSignerParameters
```

This interface encapsulates the parameters for a ContentSigner object.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
[] getCommandLine()

Retrieves the command-line arguments passed to the jarsigner tool.

**Returns:**
- The command-line arguments. May be null.

---

#### URI
getTimestampingAuthority()

Retrieves the identifier for a Timestamping Authority (TSA).

**Returns:**
- The TSA identifier. May be null.

---

#### X509Certificate
getTimestampingAuthorityCertificate()

Retrieves the certificate for a Timestamping Authority (TSA).

**Returns:**
- The TSA certificate. May be null.

---

#### default
String
getTSAPolicyID()

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

**Returns:**
- The TSAPolicyID. May be null.

---

#### default
String
getTSADigestAlg()

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

**Returns:**
- The non-null string of the message digest algorithm name.

**Since:**
- 9

---

#### byte[] getSignature()

Retrieves the JAR file's signature.

**Returns:**
- The non-null array of signature bytes.

---

#### String
getSignatureAlgorithm()

Retrieves the name of the signature algorithm.

**Returns:**
- The non-null string name of the signature algorithm.

---

#### X509Certificate
[] getSignerCertificateChain()

Retrieves the signer's X.509 certificate chain.

**Returns:**
- The non-null array of X.509 public-key certificates.

---

#### byte[] getContent()

Retrieves the content that was signed.
The content is the JAR file's signature file.

**Returns:**
- The content bytes. May be null.

---

#### ZipFile
getSource()

Retrieves the original source ZIP file before it was signed.

**Returns:**
- The original ZIP file. May be null.

---

### Additional Sections

#### Interface ContentSignerParameters

```java
@Deprecated
(
since
="9")
public interface
ContentSignerParameters
```

Deprecated.

This class has been deprecated.

This interface encapsulates the parameters for a ContentSigner object.

**Since:** 1.5

@Deprecated

(

since

="9")
public interface

ContentSignerParameters

This interface encapsulates the parameters for a ContentSigner object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

String

[]

getCommandLine

()

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

byte[]

getContent

()

Deprecated.

Retrieves the content that was signed.

byte[]

getSignature

()

Deprecated.

Retrieves the JAR file's signature.

String

getSignatureAlgorithm

()

Deprecated.

Retrieves the name of the signature algorithm.

X509Certificate

[]

getSignerCertificateChain

()

Deprecated.

Retrieves the signer's X.509 certificate chain.

ZipFile

getSource

()

Deprecated.

Retrieves the original source ZIP file before it was signed.

URI

getTimestampingAuthority

()

Deprecated.

Retrieves the identifier for a Timestamping Authority (TSA).

X509Certificate

getTimestampingAuthorityCertificate

()

Deprecated.

Retrieves the certificate for a Timestamping Authority (TSA).

default

String

getTSADigestAlg

()

Deprecated.

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

default

String

getTSAPolicyID

()

Deprecated.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

String

[]

getCommandLine

()

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

byte[]

getContent

()

Deprecated.

Retrieves the content that was signed.

byte[]

getSignature

()

Deprecated.

Retrieves the JAR file's signature.

String

getSignatureAlgorithm

()

Deprecated.

Retrieves the name of the signature algorithm.

X509Certificate

[]

getSignerCertificateChain

()

Deprecated.

Retrieves the signer's X.509 certificate chain.

ZipFile

getSource

()

Deprecated.

Retrieves the original source ZIP file before it was signed.

URI

getTimestampingAuthority

()

Deprecated.

Retrieves the identifier for a Timestamping Authority (TSA).

X509Certificate

getTimestampingAuthorityCertificate

()

Deprecated.

Retrieves the certificate for a Timestamping Authority (TSA).

default

String

getTSADigestAlg

()

Deprecated.

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

default

String

getTSAPolicyID

()

Deprecated.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

---

#### Method Summary

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

Retrieves the content that was signed.

Retrieves the JAR file's signature.

Retrieves the name of the signature algorithm.

Retrieves the signer's X.509 certificate chain.

Retrieves the original source ZIP file before it was signed.

Retrieves the identifier for a Timestamping Authority (TSA).

Retrieves the certificate for a Timestamping Authority (TSA).

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

============ METHOD DETAIL ==========

- Method Detail

- getCommandLine

```java
String
[] getCommandLine()
```

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

**Returns:** The command-line arguments. May be null.

- getTimestampingAuthority

```java
URI
getTimestampingAuthority()
```

Deprecated.

Retrieves the identifier for a Timestamping Authority (TSA).

**Returns:** The TSA identifier. May be null.

- getTimestampingAuthorityCertificate

```java
X509Certificate
getTimestampingAuthorityCertificate()
```

Deprecated.

Retrieves the certificate for a Timestamping Authority (TSA).

**Returns:** The TSA certificate. May be null.

- getTSAPolicyID

```java
default
String
getTSAPolicyID()
```

Deprecated.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

**Returns:** The TSAPolicyID. May be null.

- getTSADigestAlg

```java
default
String
getTSADigestAlg()
```

Deprecated.

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

**Returns:** The non-null string of the message digest algorithm name.
**Since:** 9

- getSignature

```java
byte[] getSignature()
```

Deprecated.

Retrieves the JAR file's signature.

**Returns:** The non-null array of signature bytes.

- getSignatureAlgorithm

```java
String
getSignatureAlgorithm()
```

Deprecated.

Retrieves the name of the signature algorithm.

**Returns:** The non-null string name of the signature algorithm.

- getSignerCertificateChain

```java
X509Certificate
[] getSignerCertificateChain()
```

Deprecated.

Retrieves the signer's X.509 certificate chain.

**Returns:** The non-null array of X.509 public-key certificates.

- getContent

```java
byte[] getContent()
```

Deprecated.

Retrieves the content that was signed.
The content is the JAR file's signature file.

**Returns:** The content bytes. May be null.

- getSource

```java
ZipFile
getSource()
```

Deprecated.

Retrieves the original source ZIP file before it was signed.

**Returns:** The original ZIP file. May be null.

Method Detail

- getCommandLine

```java
String
[] getCommandLine()
```

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

**Returns:** The command-line arguments. May be null.

- getTimestampingAuthority

```java
URI
getTimestampingAuthority()
```

Deprecated.

Retrieves the identifier for a Timestamping Authority (TSA).

**Returns:** The TSA identifier. May be null.

- getTimestampingAuthorityCertificate

```java
X509Certificate
getTimestampingAuthorityCertificate()
```

Deprecated.

Retrieves the certificate for a Timestamping Authority (TSA).

**Returns:** The TSA certificate. May be null.

- getTSAPolicyID

```java
default
String
getTSAPolicyID()
```

Deprecated.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

**Returns:** The TSAPolicyID. May be null.

- getTSADigestAlg

```java
default
String
getTSADigestAlg()
```

Deprecated.

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

**Returns:** The non-null string of the message digest algorithm name.
**Since:** 9

- getSignature

```java
byte[] getSignature()
```

Deprecated.

Retrieves the JAR file's signature.

**Returns:** The non-null array of signature bytes.

- getSignatureAlgorithm

```java
String
getSignatureAlgorithm()
```

Deprecated.

Retrieves the name of the signature algorithm.

**Returns:** The non-null string name of the signature algorithm.

- getSignerCertificateChain

```java
X509Certificate
[] getSignerCertificateChain()
```

Deprecated.

Retrieves the signer's X.509 certificate chain.

**Returns:** The non-null array of X.509 public-key certificates.

- getContent

```java
byte[] getContent()
```

Deprecated.

Retrieves the content that was signed.
The content is the JAR file's signature file.

**Returns:** The content bytes. May be null.

- getSource

```java
ZipFile
getSource()
```

Deprecated.

Retrieves the original source ZIP file before it was signed.

**Returns:** The original ZIP file. May be null.

---

#### Method Detail

getCommandLine

```java
String
[] getCommandLine()
```

Deprecated.

Retrieves the command-line arguments passed to the jarsigner tool.

**Returns:** The command-line arguments. May be null.

---

#### getCommandLine

String

[] getCommandLine()

Retrieves the command-line arguments passed to the jarsigner tool.

getTimestampingAuthority

```java
URI
getTimestampingAuthority()
```

Deprecated.

Retrieves the identifier for a Timestamping Authority (TSA).

**Returns:** The TSA identifier. May be null.

---

#### getTimestampingAuthority

URI

getTimestampingAuthority()

Retrieves the identifier for a Timestamping Authority (TSA).

getTimestampingAuthorityCertificate

```java
X509Certificate
getTimestampingAuthorityCertificate()
```

Deprecated.

Retrieves the certificate for a Timestamping Authority (TSA).

**Returns:** The TSA certificate. May be null.

---

#### getTimestampingAuthorityCertificate

X509Certificate

getTimestampingAuthorityCertificate()

Retrieves the certificate for a Timestamping Authority (TSA).

getTSAPolicyID

```java
default
String
getTSAPolicyID()
```

Deprecated.

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

**Returns:** The TSAPolicyID. May be null.

---

#### getTSAPolicyID

default

String

getTSAPolicyID()

Retrieves the TSAPolicyID for a Timestamping Authority (TSA).

getTSADigestAlg

```java
default
String
getTSADigestAlg()
```

Deprecated.

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

**Returns:** The non-null string of the message digest algorithm name.
**Since:** 9

---

#### getTSADigestAlg

default

String

getTSADigestAlg()

Retreives the message digest algorithm that is used to generate
the message imprint to be sent to the TSA server.

getSignature

```java
byte[] getSignature()
```

Deprecated.

Retrieves the JAR file's signature.

**Returns:** The non-null array of signature bytes.

---

#### getSignature

byte[] getSignature()

Retrieves the JAR file's signature.

getSignatureAlgorithm

```java
String
getSignatureAlgorithm()
```

Deprecated.

Retrieves the name of the signature algorithm.

**Returns:** The non-null string name of the signature algorithm.

---

#### getSignatureAlgorithm

String

getSignatureAlgorithm()

Retrieves the name of the signature algorithm.

getSignerCertificateChain

```java
X509Certificate
[] getSignerCertificateChain()
```

Deprecated.

Retrieves the signer's X.509 certificate chain.

**Returns:** The non-null array of X.509 public-key certificates.

---

#### getSignerCertificateChain

X509Certificate

[] getSignerCertificateChain()

Retrieves the signer's X.509 certificate chain.

getContent

```java
byte[] getContent()
```

Deprecated.

Retrieves the content that was signed.
The content is the JAR file's signature file.

**Returns:** The content bytes. May be null.

---

#### getContent

byte[] getContent()

Retrieves the content that was signed.
The content is the JAR file's signature file.

getSource

```java
ZipFile
getSource()
```

Deprecated.

Retrieves the original source ZIP file before it was signed.

**Returns:** The original ZIP file. May be null.

---

#### getSource

ZipFile

getSource()

Retrieves the original source ZIP file before it was signed.

---

