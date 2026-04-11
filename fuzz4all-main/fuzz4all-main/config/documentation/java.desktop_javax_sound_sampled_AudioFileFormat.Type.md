# Class AudioFileFormat.Type

**Source:** `java.desktop\javax\sound\sampled\AudioFileFormat.Type.html`

### Class Description

```java
public static class
AudioFileFormat.Type

extends
Object
```

An instance of the

Type

class represents one of the standard
types of audio file. Static instances are provided for the common types.

**Enclosing class:** AudioFileFormat

---

### Field Details

#### public static final
AudioFileFormat.Type
WAVE

Specifies a WAVE file.

---

#### public static final
AudioFileFormat.Type
AU

Specifies an AU file.

---

#### public static final
AudioFileFormat.Type
AIFF

Specifies an AIFF file.

---

#### public static final
AudioFileFormat.Type
AIFC

Specifies an AIFF-C file.

---

#### public static final
AudioFileFormat.Type
SND

Specifies a SND file.

---

### Constructor Details

#### public Type​(
String
name,

String
extension)

Constructs a file type.

**Parameters:**
- name

- the string that names the file type
- extension

- the string that commonly marks the file type
without leading dot

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare

**Returns:**
- true

if the specified object is equal to this file
type;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this file type.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this file type

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
toString()

Provides the file type's name as the

String

representation of
the file type.

**Overrides:**
- toString

in class

Object

**Returns:**
- the file type's name

---

#### public
String
getExtension()

Obtains the common file name extension for this file type.

**Returns:**
- file type extension

---

### Additional Sections

#### Class AudioFileFormat.Type

java.lang.Object

- javax.sound.sampled.AudioFileFormat.Type

javax.sound.sampled.AudioFileFormat.Type

**Enclosing class:** AudioFileFormat

```java
public static class
AudioFileFormat.Type

extends
Object
```

An instance of the

Type

class represents one of the standard
types of audio file. Static instances are provided for the common types.

public static class

AudioFileFormat.Type

extends

Object

An instance of the

Type

class represents one of the standard
types of audio file. Static instances are provided for the common types.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AudioFileFormat.Type

AIFC

Specifies an AIFF-C file.

static

AudioFileFormat.Type

AIFF

Specifies an AIFF file.

static

AudioFileFormat.Type

AU

Specifies an AU file.

static

AudioFileFormat.Type

SND

Specifies a SND file.

static

AudioFileFormat.Type

WAVE

Specifies a WAVE file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Type

​(

String

name,

String

extension)

Constructs a file type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

String

getExtension

()

Obtains the common file name extension for this file type.

int

hashCode

()

Returns a hash code value for this file type.

String

toString

()

Provides the file type's name as the

String

representation of
the file type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

AudioFileFormat.Type

AIFC

Specifies an AIFF-C file.

static

AudioFileFormat.Type

AIFF

Specifies an AIFF file.

static

AudioFileFormat.Type

AU

Specifies an AU file.

static

AudioFileFormat.Type

SND

Specifies a SND file.

static

AudioFileFormat.Type

WAVE

Specifies a WAVE file.

---

#### Field Summary

Specifies an AIFF-C file.

Specifies an AIFF file.

Specifies an AU file.

Specifies a SND file.

Specifies a WAVE file.

Constructor Summary

Constructors

Constructor

Description

Type

​(

String

name,

String

extension)

Constructs a file type.

---

#### Constructor Summary

Constructs a file type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

String

getExtension

()

Obtains the common file name extension for this file type.

int

hashCode

()

Returns a hash code value for this file type.

String

toString

()

Provides the file type's name as the

String

representation of
the file type.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

Obtains the common file name extension for this file type.

Returns a hash code value for this file type.

Provides the file type's name as the

String

representation of
the file type.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- WAVE

```java
public static final
AudioFileFormat.Type
WAVE
```

Specifies a WAVE file.

- AU

```java
public static final
AudioFileFormat.Type
AU
```

Specifies an AU file.

- AIFF

```java
public static final
AudioFileFormat.Type
AIFF
```

Specifies an AIFF file.

- AIFC

```java
public static final
AudioFileFormat.Type
AIFC
```

Specifies an AIFF-C file.

- SND

```java
public static final
AudioFileFormat.Type
SND
```

Specifies a SND file.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Type

```java
public Type​(
String
name,

String
extension)
```

Constructs a file type.

**Parameters:** name

- the string that names the file type
**Parameters:** extension

- the string that commonly marks the file type
without leading dot

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this file
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this file type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this file type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the file type's name as the

String

representation of
the file type.

**Overrides:** toString

in class

Object
**Returns:** the file type's name

- getExtension

```java
public
String
getExtension()
```

Obtains the common file name extension for this file type.

**Returns:** file type extension

Field Detail

- WAVE

```java
public static final
AudioFileFormat.Type
WAVE
```

Specifies a WAVE file.

- AU

```java
public static final
AudioFileFormat.Type
AU
```

Specifies an AU file.

- AIFF

```java
public static final
AudioFileFormat.Type
AIFF
```

Specifies an AIFF file.

- AIFC

```java
public static final
AudioFileFormat.Type
AIFC
```

Specifies an AIFF-C file.

- SND

```java
public static final
AudioFileFormat.Type
SND
```

Specifies a SND file.

---

#### Field Detail

WAVE

```java
public static final
AudioFileFormat.Type
WAVE
```

Specifies a WAVE file.

---

#### WAVE

public static final

AudioFileFormat.Type

WAVE

Specifies a WAVE file.

AU

```java
public static final
AudioFileFormat.Type
AU
```

Specifies an AU file.

---

#### AU

public static final

AudioFileFormat.Type

AU

Specifies an AU file.

AIFF

```java
public static final
AudioFileFormat.Type
AIFF
```

Specifies an AIFF file.

---

#### AIFF

public static final

AudioFileFormat.Type

AIFF

Specifies an AIFF file.

AIFC

```java
public static final
AudioFileFormat.Type
AIFC
```

Specifies an AIFF-C file.

---

#### AIFC

public static final

AudioFileFormat.Type

AIFC

Specifies an AIFF-C file.

SND

```java
public static final
AudioFileFormat.Type
SND
```

Specifies a SND file.

---

#### SND

public static final

AudioFileFormat.Type

SND

Specifies a SND file.

Constructor Detail

- Type

```java
public Type​(
String
name,

String
extension)
```

Constructs a file type.

**Parameters:** name

- the string that names the file type
**Parameters:** extension

- the string that commonly marks the file type
without leading dot

---

#### Constructor Detail

Type

```java
public Type​(
String
name,

String
extension)
```

Constructs a file type.

**Parameters:** name

- the string that names the file type
**Parameters:** extension

- the string that commonly marks the file type
without leading dot

---

#### Type

public Type​(

String

name,

String

extension)

Constructs a file type.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this file
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this file type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this file type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the file type's name as the

String

representation of
the file type.

**Overrides:** toString

in class

Object
**Returns:** the file type's name

- getExtension

```java
public
String
getExtension()
```

Obtains the common file name extension for this file type.

**Returns:** file type extension

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this file
type;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public final boolean equals​(

Object

obj)

Indicates whether the specified object is equal to this file type,
returning

true

if the objects are equal.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this file type.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this file type
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this file type.

toString

```java
public final
String
toString()
```

Provides the file type's name as the

String

representation of
the file type.

**Overrides:** toString

in class

Object
**Returns:** the file type's name

---

#### toString

public final

String

toString()

Provides the file type's name as the

String

representation of
the file type.

getExtension

```java
public
String
getExtension()
```

Obtains the common file name extension for this file type.

**Returns:** file type extension

---

#### getExtension

public

String

getExtension()

Obtains the common file name extension for this file type.

---

