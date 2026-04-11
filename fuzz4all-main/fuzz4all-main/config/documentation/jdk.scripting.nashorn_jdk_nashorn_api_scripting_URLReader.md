# Class URLReader

**Source:** `jdk.scripting.nashorn\jdk\nashorn\api\scripting\URLReader.html`

### Class Description

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
URLReader

extends
Reader
```

A Reader that reads from a URL. Used to make sure that the reader
reads content from given URL and can be trusted to do so.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

---

### Field Details

*No entries found.*

### Constructor Details

#### public URLReader​(
URL
url)

Constructor

**Parameters:**
- url

- URL for this URLReader

**Throws:**
- NullPointerException

- if url is null

---

#### public URLReader​(
URL
url,

String
charsetName)

Constructor

**Parameters:**
- url

- URL for this URLReader
- charsetName

- Name of the Charset used to convert bytes to chars

**Throws:**
- NullPointerException

- if url is null

---

#### public URLReader​(
URL
url,

Charset
cs)

Constructor

**Parameters:**
- url

- URL for this URLReader
- cs

- Charset used to convert bytes to chars

**Throws:**
- NullPointerException

- if url is null

---

### Method Details

#### public
URL
getURL()

URL of this reader

**Returns:**
- the URL from which this reader reads.

---

#### public
Charset
getCharset()

Charset used by this reader

**Returns:**
- the Charset used to convert bytes to chars

---

### Additional Sections

#### Class URLReader

java.lang.Object

- java.io.Reader
- - jdk.nashorn.api.scripting.URLReader

java.io.Reader

- jdk.nashorn.api.scripting.URLReader

jdk.nashorn.api.scripting.URLReader

**All Implemented Interfaces:** Closeable

,

AutoCloseable

,

Readable

```java
@Deprecated
(
since
="11",

forRemoval
=true)
public final class
URLReader

extends
Reader
```

Deprecated, for removal: This API element is subject to removal in a future version.

Nashorn JavaScript script engine and APIs, and the jjs tool
are deprecated with the intent to remove them in a future release.

A Reader that reads from a URL. Used to make sure that the reader
reads content from given URL and can be trusted to do so.

**Since:** 1.8u40

@Deprecated

(

since

="11",

forRemoval

=true)
public final class

URLReader

extends

Reader

A Reader that reads from a URL. Used to make sure that the reader
reads content from given URL and can be trusted to do so.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

Reader

lock

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URLReader

​(

URL

url)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

URLReader

​(

URL

url,

String

charsetName)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

URLReader

​(

URL

url,

Charset

cs)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Charset

getCharset

()

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

URL

getURL

()

Deprecated, for removal: This API element is subject to removal in a future version.

URL of this reader

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

read

,

read

,

ready

,

reset

,

skip

,

transferTo

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.io.

Reader

lock

---

#### Field Summary

Fields declared in class java.io.

Reader

lock

---

#### Fields declared in class java.io. Reader

Constructor Summary

Constructors

Constructor

Description

URLReader

​(

URL

url)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

URLReader

​(

URL

url,

String

charsetName)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

URLReader

​(

URL

url,

Charset

cs)

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

---

#### Constructor Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Charset

getCharset

()

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

URL

getURL

()

Deprecated, for removal: This API element is subject to removal in a future version.

URL of this reader

- Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

read

,

read

,

ready

,

reset

,

skip

,

transferTo

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

URL of this reader

Methods declared in class java.io.

Reader

close

,

mark

,

markSupported

,

nullReader

,

read

,

read

,

read

,

read

,

ready

,

reset

,

skip

,

transferTo

---

#### Methods declared in class java.io. Reader

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- URLReader

```java
public URLReader​(
URL
url)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Throws:** NullPointerException

- if url is null

- URLReader

```java
public URLReader​(
URL
url,

String
charsetName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** charsetName

- Name of the Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

- URLReader

```java
public URLReader​(
URL
url,

Charset
cs)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** cs

- Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

============ METHOD DETAIL ==========

- Method Detail

- getURL

```java
public
URL
getURL()
```

Deprecated, for removal: This API element is subject to removal in a future version.

URL of this reader

**Returns:** the URL from which this reader reads.

- getCharset

```java
public
Charset
getCharset()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

**Returns:** the Charset used to convert bytes to chars

Constructor Detail

- URLReader

```java
public URLReader​(
URL
url)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Throws:** NullPointerException

- if url is null

- URLReader

```java
public URLReader​(
URL
url,

String
charsetName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** charsetName

- Name of the Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

- URLReader

```java
public URLReader​(
URL
url,

Charset
cs)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** cs

- Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

---

#### Constructor Detail

URLReader

```java
public URLReader​(
URL
url)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Throws:** NullPointerException

- if url is null

---

#### URLReader

public URLReader​(

URL

url)

Constructor

URLReader

```java
public URLReader​(
URL
url,

String
charsetName)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** charsetName

- Name of the Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

---

#### URLReader

public URLReader​(

URL

url,

String

charsetName)

Constructor

URLReader

```java
public URLReader​(
URL
url,

Charset
cs)
```

Deprecated, for removal: This API element is subject to removal in a future version.

Constructor

**Parameters:** url

- URL for this URLReader
**Parameters:** cs

- Charset used to convert bytes to chars
**Throws:** NullPointerException

- if url is null

---

#### URLReader

public URLReader​(

URL

url,

Charset

cs)

Constructor

Method Detail

- getURL

```java
public
URL
getURL()
```

Deprecated, for removal: This API element is subject to removal in a future version.

URL of this reader

**Returns:** the URL from which this reader reads.

- getCharset

```java
public
Charset
getCharset()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

**Returns:** the Charset used to convert bytes to chars

---

#### Method Detail

getURL

```java
public
URL
getURL()
```

Deprecated, for removal: This API element is subject to removal in a future version.

URL of this reader

**Returns:** the URL from which this reader reads.

---

#### getURL

public

URL

getURL()

URL of this reader

getCharset

```java
public
Charset
getCharset()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Charset used by this reader

**Returns:** the Charset used to convert bytes to chars

---

#### getCharset

public

Charset

getCharset()

Charset used by this reader

---

