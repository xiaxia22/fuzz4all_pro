# Class ImageTranscoderSpi

**Source:** `java.desktop\javax\imageio\spi\ImageTranscoderSpi.html`

### Class Description

```java
public abstract class
ImageTranscoderSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageTranscoder

s.
For more information on service provider classes, see the class comment
for the

IIORegistry

class.

**All Implemented Interfaces:** RegisterableService

---

### Field Details

*No entries found.*

### Constructor Details

#### protected ImageTranscoderSpi()

Constructs a blank

ImageTranscoderSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### public ImageTranscoderSpi​(
String
vendorName,

String
version)

Constructs an

ImageTranscoderSpi

with a given set
of values.

**Parameters:**
- vendorName

- the vendor name.
- version

- a version identifier.

---

### Method Details

#### public abstract
String
getReaderServiceProviderName()

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:**
- a

String

containing the fully-qualified
class name of the

ImageReaderSpi

implementation class.

**See Also:**
- ImageReaderSpi

---

#### public abstract
String
getWriterServiceProviderName()

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:**
- a

String

containing the fully-qualified
class name of the

ImageWriterSpi

implementation class.

**See Also:**
- ImageWriterSpi

---

#### public abstract
ImageTranscoder
createTranscoderInstance()

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

**Returns:**
- an

ImageTranscoder

instance.

---

### Additional Sections

#### Class ImageTranscoderSpi

java.lang.Object

- javax.imageio.spi.IIOServiceProvider
- - javax.imageio.spi.ImageTranscoderSpi

javax.imageio.spi.IIOServiceProvider

- javax.imageio.spi.ImageTranscoderSpi

javax.imageio.spi.ImageTranscoderSpi

**All Implemented Interfaces:** RegisterableService

```java
public abstract class
ImageTranscoderSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageTranscoder

s.
For more information on service provider classes, see the class comment
for the

IIORegistry

class.

**See Also:** IIORegistry

,

ImageTranscoder

public abstract class

ImageTranscoderSpi

extends

IIOServiceProvider

The service provider interface (SPI) for

ImageTranscoder

s.
For more information on service provider classes, see the class comment
for the

IIORegistry

class.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ImageTranscoderSpi

()

Constructs a blank

ImageTranscoderSpi

.

ImageTranscoderSpi

​(

String

vendorName,

String

version)

Constructs an

ImageTranscoderSpi

with a given set
of values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

ImageTranscoder

createTranscoderInstance

()

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

abstract

String

getReaderServiceProviderName

()

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

abstract

String

getWriterServiceProviderName

()

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

- Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

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

- Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

---

#### Field Summary

Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

---

#### Fields declared in class javax.imageio.spi. IIOServiceProvider

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ImageTranscoderSpi

()

Constructs a blank

ImageTranscoderSpi

.

ImageTranscoderSpi

​(

String

vendorName,

String

version)

Constructs an

ImageTranscoderSpi

with a given set
of values.

---

#### Constructor Summary

Constructs a blank

ImageTranscoderSpi

.

Constructs an

ImageTranscoderSpi

with a given set
of values.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

ImageTranscoder

createTranscoderInstance

()

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

abstract

String

getReaderServiceProviderName

()

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

abstract

String

getWriterServiceProviderName

()

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

- Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

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

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

Methods declared in class javax.imageio.spi.

IIOServiceProvider

getDescription

,

getVendorName

,

getVersion

,

onDeregistration

,

onRegistration

---

#### Methods declared in class javax.imageio.spi. IIOServiceProvider

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

- ImageTranscoderSpi

```java
protected ImageTranscoderSpi()
```

Constructs a blank

ImageTranscoderSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageTranscoderSpi

```java
public ImageTranscoderSpi​(
String
vendorName,

String
version)
```

Constructs an

ImageTranscoderSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.

============ METHOD DETAIL ==========

- Method Detail

- getReaderServiceProviderName

```java
public abstract
String
getReaderServiceProviderName()
```

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageReaderSpi

implementation class.
**See Also:** ImageReaderSpi

- getWriterServiceProviderName

```java
public abstract
String
getWriterServiceProviderName()
```

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageWriterSpi

implementation class.
**See Also:** ImageWriterSpi

- createTranscoderInstance

```java
public abstract
ImageTranscoder
createTranscoderInstance()
```

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

**Returns:** an

ImageTranscoder

instance.

Constructor Detail

- ImageTranscoderSpi

```java
protected ImageTranscoderSpi()
```

Constructs a blank

ImageTranscoderSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageTranscoderSpi

```java
public ImageTranscoderSpi​(
String
vendorName,

String
version)
```

Constructs an

ImageTranscoderSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.

---

#### Constructor Detail

ImageTranscoderSpi

```java
protected ImageTranscoderSpi()
```

Constructs a blank

ImageTranscoderSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### ImageTranscoderSpi

protected ImageTranscoderSpi()

Constructs a blank

ImageTranscoderSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

ImageTranscoderSpi

```java
public ImageTranscoderSpi​(
String
vendorName,

String
version)
```

Constructs an

ImageTranscoderSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.

---

#### ImageTranscoderSpi

public ImageTranscoderSpi​(

String

vendorName,

String

version)

Constructs an

ImageTranscoderSpi

with a given set
of values.

Method Detail

- getReaderServiceProviderName

```java
public abstract
String
getReaderServiceProviderName()
```

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageReaderSpi

implementation class.
**See Also:** ImageReaderSpi

- getWriterServiceProviderName

```java
public abstract
String
getWriterServiceProviderName()
```

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageWriterSpi

implementation class.
**See Also:** ImageWriterSpi

- createTranscoderInstance

```java
public abstract
ImageTranscoder
createTranscoderInstance()
```

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

**Returns:** an

ImageTranscoder

instance.

---

#### Method Detail

getReaderServiceProviderName

```java
public abstract
String
getReaderServiceProviderName()
```

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageReaderSpi

implementation class.
**See Also:** ImageReaderSpi

---

#### getReaderServiceProviderName

public abstract

String

getReaderServiceProviderName()

Returns the fully qualified class name of an

ImageReaderSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

getWriterServiceProviderName

```java
public abstract
String
getWriterServiceProviderName()
```

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

**Returns:** a

String

containing the fully-qualified
class name of the

ImageWriterSpi

implementation class.
**See Also:** ImageWriterSpi

---

#### getWriterServiceProviderName

public abstract

String

getWriterServiceProviderName()

Returns the fully qualified class name of an

ImageWriterSpi

class that generates

IIOMetadata

objects that may be used as input to
this transcoder.

createTranscoderInstance

```java
public abstract
ImageTranscoder
createTranscoderInstance()
```

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

**Returns:** an

ImageTranscoder

instance.

---

#### createTranscoderInstance

public abstract

ImageTranscoder

createTranscoderInstance()

Returns an instance of the

ImageTranscoder

implementation associated with this service provider.

---

