# Class AudioFormat.Encoding

**Source:** `java.desktop\javax\sound\sampled\AudioFormat.Encoding.html`

### Class Description

```java
public static class
AudioFormat.Encoding

extends
Object
```

The

Encoding

class names the specific type of data representation
used for an audio stream. The encoding includes aspects of the sound
format other than the number of channels, sample rate, sample size, frame
rate, frame size, and byte order.

One ubiquitous type of audio encoding is pulse-code modulation (PCM),
which is simply a linear (proportional) representation of the sound
waveform. With PCM, the number stored in each sample is proportional to
the instantaneous amplitude of the sound pressure at that point in time.
The numbers may be signed or unsigned integers or floats. Besides PCM,
other encodings include mu-law and a-law, which are nonlinear mappings of
the sound amplitude that are often used for recording speech.

You can use a predefined encoding by referring to one of the static
objects created by this class, such as

PCM_SIGNED

or

PCM_UNSIGNED

. Service providers can create new encodings, such as
compressed audio formats, and make these available through the

AudioSystem

class.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

**Enclosing class:** AudioFormat

---

### Field Details

#### public static final
AudioFormat.Encoding
PCM_SIGNED

Specifies signed, linear PCM data.

---

#### public static final
AudioFormat.Encoding
PCM_UNSIGNED

Specifies unsigned, linear PCM data.

---

#### public static final
AudioFormat.Encoding
PCM_FLOAT

Specifies floating-point PCM data.

**Since:**
- 1.7

---

#### public static final
AudioFormat.Encoding
ULAW

Specifies u-law encoded data.

---

#### public static final
AudioFormat.Encoding
ALAW

Specifies a-law encoded data.

---

### Constructor Details

#### public Encoding​(
String
name)

Constructs a new encoding.

**Parameters:**
- name

- the name of the new type of encoding

---

### Method Details

#### public final boolean equals​(
Object
obj)

Indicates whether the specified object is equal to this encoding,
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

if the specified object is equal to this
encoding;

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final int hashCode()

Returns a hash code value for this encoding.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this encoding

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public final
String
toString()

Provides the

String

representation of the encoding. This

String

is the same name that was passed to the constructor.
For the predefined encodings, the name is similar to the encoding's
variable (field) name. For example,

PCM_SIGNED.toString()

returns the name "PCM_SIGNED".

**Overrides:**
- toString

in class

Object

**Returns:**
- the encoding name

---

### Additional Sections

#### Class AudioFormat.Encoding

java.lang.Object

- javax.sound.sampled.AudioFormat.Encoding

javax.sound.sampled.AudioFormat.Encoding

**Enclosing class:** AudioFormat

```java
public static class
AudioFormat.Encoding

extends
Object
```

The

Encoding

class names the specific type of data representation
used for an audio stream. The encoding includes aspects of the sound
format other than the number of channels, sample rate, sample size, frame
rate, frame size, and byte order.

One ubiquitous type of audio encoding is pulse-code modulation (PCM),
which is simply a linear (proportional) representation of the sound
waveform. With PCM, the number stored in each sample is proportional to
the instantaneous amplitude of the sound pressure at that point in time.
The numbers may be signed or unsigned integers or floats. Besides PCM,
other encodings include mu-law and a-law, which are nonlinear mappings of
the sound amplitude that are often used for recording speech.

You can use a predefined encoding by referring to one of the static
objects created by this class, such as

PCM_SIGNED

or

PCM_UNSIGNED

. Service providers can create new encodings, such as
compressed audio formats, and make these available through the

AudioSystem

class.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

**Since:** 1.3
**See Also:** AudioFormat

,

FormatConversionProvider

public static class

AudioFormat.Encoding

extends

Object

The

Encoding

class names the specific type of data representation
used for an audio stream. The encoding includes aspects of the sound
format other than the number of channels, sample rate, sample size, frame
rate, frame size, and byte order.

One ubiquitous type of audio encoding is pulse-code modulation (PCM),
which is simply a linear (proportional) representation of the sound
waveform. With PCM, the number stored in each sample is proportional to
the instantaneous amplitude of the sound pressure at that point in time.
The numbers may be signed or unsigned integers or floats. Besides PCM,
other encodings include mu-law and a-law, which are nonlinear mappings of
the sound amplitude that are often used for recording speech.

You can use a predefined encoding by referring to one of the static
objects created by this class, such as

PCM_SIGNED

or

PCM_UNSIGNED

. Service providers can create new encodings, such as
compressed audio formats, and make these available through the

AudioSystem

class.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

One ubiquitous type of audio encoding is pulse-code modulation (PCM),
which is simply a linear (proportional) representation of the sound
waveform. With PCM, the number stored in each sample is proportional to
the instantaneous amplitude of the sound pressure at that point in time.
The numbers may be signed or unsigned integers or floats. Besides PCM,
other encodings include mu-law and a-law, which are nonlinear mappings of
the sound amplitude that are often used for recording speech.

You can use a predefined encoding by referring to one of the static
objects created by this class, such as

PCM_SIGNED

or

PCM_UNSIGNED

. Service providers can create new encodings, such as
compressed audio formats, and make these available through the

AudioSystem

class.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

You can use a predefined encoding by referring to one of the static
objects created by this class, such as

PCM_SIGNED

or

PCM_UNSIGNED

. Service providers can create new encodings, such as
compressed audio formats, and make these available through the

AudioSystem

class.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

The

Encoding

class is static, so that all

AudioFormat

objects that have the same encoding will refer to the same object (rather
than different instances of the same class). This allows matches to be
made by checking that two format's encodings are equal.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

AudioFormat.Encoding

ALAW

Specifies a-law encoded data.

static

AudioFormat.Encoding

PCM_FLOAT

Specifies floating-point PCM data.

static

AudioFormat.Encoding

PCM_SIGNED

Specifies signed, linear PCM data.

static

AudioFormat.Encoding

PCM_UNSIGNED

Specifies unsigned, linear PCM data.

static

AudioFormat.Encoding

ULAW

Specifies u-law encoded data.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Encoding

​(

String

name)

Constructs a new encoding.

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

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

int

hashCode

()

Returns a hash code value for this encoding.

String

toString

()

Provides the

String

representation of the encoding.

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

AudioFormat.Encoding

ALAW

Specifies a-law encoded data.

static

AudioFormat.Encoding

PCM_FLOAT

Specifies floating-point PCM data.

static

AudioFormat.Encoding

PCM_SIGNED

Specifies signed, linear PCM data.

static

AudioFormat.Encoding

PCM_UNSIGNED

Specifies unsigned, linear PCM data.

static

AudioFormat.Encoding

ULAW

Specifies u-law encoded data.

---

#### Field Summary

Specifies a-law encoded data.

Specifies floating-point PCM data.

Specifies signed, linear PCM data.

Specifies unsigned, linear PCM data.

Specifies u-law encoded data.

Constructor Summary

Constructors

Constructor

Description

Encoding

​(

String

name)

Constructs a new encoding.

---

#### Constructor Summary

Constructs a new encoding.

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

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

int

hashCode

()

Returns a hash code value for this encoding.

String

toString

()

Provides the

String

representation of the encoding.

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

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

Returns a hash code value for this encoding.

Provides the

String

representation of the encoding.

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

- PCM_SIGNED

```java
public static final
AudioFormat.Encoding
PCM_SIGNED
```

Specifies signed, linear PCM data.

- PCM_UNSIGNED

```java
public static final
AudioFormat.Encoding
PCM_UNSIGNED
```

Specifies unsigned, linear PCM data.

- PCM_FLOAT

```java
public static final
AudioFormat.Encoding
PCM_FLOAT
```

Specifies floating-point PCM data.

**Since:** 1.7

- ULAW

```java
public static final
AudioFormat.Encoding
ULAW
```

Specifies u-law encoded data.

- ALAW

```java
public static final
AudioFormat.Encoding
ALAW
```

Specifies a-law encoded data.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Encoding

```java
public Encoding​(
String
name)
```

Constructs a new encoding.

**Parameters:** name

- the name of the new type of encoding

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
encoding;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this encoding.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this encoding
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the

String

representation of the encoding. This

String

is the same name that was passed to the constructor.
For the predefined encodings, the name is similar to the encoding's
variable (field) name. For example,

PCM_SIGNED.toString()

returns the name "PCM_SIGNED".

**Overrides:** toString

in class

Object
**Returns:** the encoding name

Field Detail

- PCM_SIGNED

```java
public static final
AudioFormat.Encoding
PCM_SIGNED
```

Specifies signed, linear PCM data.

- PCM_UNSIGNED

```java
public static final
AudioFormat.Encoding
PCM_UNSIGNED
```

Specifies unsigned, linear PCM data.

- PCM_FLOAT

```java
public static final
AudioFormat.Encoding
PCM_FLOAT
```

Specifies floating-point PCM data.

**Since:** 1.7

- ULAW

```java
public static final
AudioFormat.Encoding
ULAW
```

Specifies u-law encoded data.

- ALAW

```java
public static final
AudioFormat.Encoding
ALAW
```

Specifies a-law encoded data.

---

#### Field Detail

PCM_SIGNED

```java
public static final
AudioFormat.Encoding
PCM_SIGNED
```

Specifies signed, linear PCM data.

---

#### PCM_SIGNED

public static final

AudioFormat.Encoding

PCM_SIGNED

Specifies signed, linear PCM data.

PCM_UNSIGNED

```java
public static final
AudioFormat.Encoding
PCM_UNSIGNED
```

Specifies unsigned, linear PCM data.

---

#### PCM_UNSIGNED

public static final

AudioFormat.Encoding

PCM_UNSIGNED

Specifies unsigned, linear PCM data.

PCM_FLOAT

```java
public static final
AudioFormat.Encoding
PCM_FLOAT
```

Specifies floating-point PCM data.

**Since:** 1.7

---

#### PCM_FLOAT

public static final

AudioFormat.Encoding

PCM_FLOAT

Specifies floating-point PCM data.

ULAW

```java
public static final
AudioFormat.Encoding
ULAW
```

Specifies u-law encoded data.

---

#### ULAW

public static final

AudioFormat.Encoding

ULAW

Specifies u-law encoded data.

ALAW

```java
public static final
AudioFormat.Encoding
ALAW
```

Specifies a-law encoded data.

---

#### ALAW

public static final

AudioFormat.Encoding

ALAW

Specifies a-law encoded data.

Constructor Detail

- Encoding

```java
public Encoding​(
String
name)
```

Constructs a new encoding.

**Parameters:** name

- the name of the new type of encoding

---

#### Constructor Detail

Encoding

```java
public Encoding​(
String
name)
```

Constructs a new encoding.

**Parameters:** name

- the name of the new type of encoding

---

#### Encoding

public Encoding​(

String

name)

Constructs a new encoding.

Method Detail

- equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
encoding;

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public final int hashCode()
```

Returns a hash code value for this encoding.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this encoding
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public final
String
toString()
```

Provides the

String

representation of the encoding. This

String

is the same name that was passed to the constructor.
For the predefined encodings, the name is similar to the encoding's
variable (field) name. For example,

PCM_SIGNED.toString()

returns the name "PCM_SIGNED".

**Overrides:** toString

in class

Object
**Returns:** the encoding name

---

#### Method Detail

equals

```java
public final boolean equals​(
Object
obj)
```

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare
**Returns:** true

if the specified object is equal to this
encoding;

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

Indicates whether the specified object is equal to this encoding,
returning

true

if the objects are equal.

hashCode

```java
public final int hashCode()
```

Returns a hash code value for this encoding.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this encoding
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hash code value for this encoding.

toString

```java
public final
String
toString()
```

Provides the

String

representation of the encoding. This

String

is the same name that was passed to the constructor.
For the predefined encodings, the name is similar to the encoding's
variable (field) name. For example,

PCM_SIGNED.toString()

returns the name "PCM_SIGNED".

**Overrides:** toString

in class

Object
**Returns:** the encoding name

---

#### toString

public final

String

toString()

Provides the

String

representation of the encoding. This

String

is the same name that was passed to the constructor.
For the predefined encodings, the name is similar to the encoding's
variable (field) name. For example,

PCM_SIGNED.toString()

returns the name "PCM_SIGNED".

---

