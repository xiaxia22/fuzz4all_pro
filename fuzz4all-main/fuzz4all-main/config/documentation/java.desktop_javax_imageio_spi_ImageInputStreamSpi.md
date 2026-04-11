# Class ImageInputStreamSpi

**Source:** `java.desktop\javax\imageio\spi\ImageInputStreamSpi.html`

### Class Description

```java
public abstract class
ImageInputStreamSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageInputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageInputStream

. For example,
a particular

ImageInputStreamSpi

might allow
a generic

InputStream

to be used as an input source;
another might take input from a

URL

.

By treating the creation of

ImageInputStream

s as a
pluggable service, it becomes possible to handle future input
sources without changing the API. Also, high-performance
implementations of

ImageInputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

**All Implemented Interfaces:** RegisterableService

---

### Field Details

#### protected
Class
<?> inputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

### Constructor Details

#### protected ImageInputStreamSpi()

Constructs a blank

ImageInputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### public ImageInputStreamSpi​(
String
vendorName,

String
version,

Class
<?> inputClass)

Constructs an

ImageInputStreamSpi

with a given set
of values.

**Parameters:**
- vendorName

- the vendor name.
- version

- a version identifier.
- inputClass

- a

Class

object indicating the
legal object type for use by the

createInputStreamInstance

method.

**Throws:**
- IllegalArgumentException

- if

vendorName

is

null

.
- IllegalArgumentException

- if

version

is

null

.

---

### Method Details

#### public
Class
<?> getInputClass()

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

**Returns:**
- a

Class

variable.

**See Also:**
- createInputStreamInstance(Object, boolean, File)

---

#### public boolean canUseCacheFile()

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint. If

false

, the value of
the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:**
- true

if a cache file can be used by the
input streams created by this service provider.

---

#### public boolean needsCacheFile()

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

. If

true

,
the value of the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:**
- true

if a cache file is needed by the
input streams created by this service provider.

---

#### public abstract
ImageInputStream
createInputStreamInstance​(
Object
input,
boolean useCache,

File
cacheDir)
throws
IOException

Returns an instance of the

ImageInputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:**
- input

- an object of the class type returned by

getInputClass

.
- useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
- cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.

**Returns:**
- an

ImageInputStream

instance.

**Throws:**
- IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
- IllegalArgumentException

- if a cache file is needed
but

cacheDir

is non-

null

and is not a
directory.
- IOException

- if a cache file is needed but cannot be
created.

**See Also:**
- getInputClass()

,

canUseCacheFile()

,

needsCacheFile()

---

#### public
ImageInputStream
createInputStreamInstance​(
Object
input)
throws
IOException

Returns an instance of the

ImageInputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:**
- input

- an object of the class type returned by

getInputClass

.

**Returns:**
- an

ImageInputStream

instance.

**Throws:**
- IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
- IOException

- if a cache file is needed but cannot be
created.

**See Also:**
- getInputClass()

---

### Additional Sections

#### Class ImageInputStreamSpi

java.lang.Object

- javax.imageio.spi.IIOServiceProvider
- - javax.imageio.spi.ImageInputStreamSpi

javax.imageio.spi.IIOServiceProvider

- javax.imageio.spi.ImageInputStreamSpi

javax.imageio.spi.ImageInputStreamSpi

**All Implemented Interfaces:** RegisterableService

```java
public abstract class
ImageInputStreamSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageInputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageInputStream

. For example,
a particular

ImageInputStreamSpi

might allow
a generic

InputStream

to be used as an input source;
another might take input from a

URL

.

By treating the creation of

ImageInputStream

s as a
pluggable service, it becomes possible to handle future input
sources without changing the API. Also, high-performance
implementations of

ImageInputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

**See Also:** IIORegistry

,

ImageInputStream

public abstract class

ImageInputStreamSpi

extends

IIOServiceProvider

The service provider interface (SPI) for

ImageInputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageInputStream

. For example,
a particular

ImageInputStreamSpi

might allow
a generic

InputStream

to be used as an input source;
another might take input from a

URL

.

By treating the creation of

ImageInputStream

s as a
pluggable service, it becomes possible to handle future input
sources without changing the API. Also, high-performance
implementations of

ImageInputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageInputStream

. For example,
a particular

ImageInputStreamSpi

might allow
a generic

InputStream

to be used as an input source;
another might take input from a

URL

.

By treating the creation of

ImageInputStream

s as a
pluggable service, it becomes possible to handle future input
sources without changing the API. Also, high-performance
implementations of

ImageInputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

By treating the creation of

ImageInputStream

s as a
pluggable service, it becomes possible to handle future input
sources without changing the API. Also, high-performance
implementations of

ImageInputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Class

<?>

inputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

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

ImageInputStreamSpi

()

Constructs a blank

ImageInputStreamSpi

.

ImageInputStreamSpi

​(

String

vendorName,

String

version,

Class

<?> inputClass)

Constructs an

ImageInputStreamSpi

with a given set
of values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canUseCacheFile

()

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint.

ImageInputStream

createInputStreamInstance

​(

Object

input)

Returns an instance of the

ImageInputStream

implementation associated with this service provider.

abstract

ImageInputStream

createInputStreamInstance

​(

Object

input,
boolean useCache,

File

cacheDir)

Returns an instance of the

ImageInputStream

implementation associated with this service provider.

Class

<?>

getInputClass

()

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

boolean

needsCacheFile

()

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

.

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

Fields

Modifier and Type

Field

Description

protected

Class

<?>

inputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

- Fields declared in class javax.imageio.spi.

IIOServiceProvider

vendorName

,

version

---

#### Field Summary

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

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

ImageInputStreamSpi

()

Constructs a blank

ImageInputStreamSpi

.

ImageInputStreamSpi

​(

String

vendorName,

String

version,

Class

<?> inputClass)

Constructs an

ImageInputStreamSpi

with a given set
of values.

---

#### Constructor Summary

Constructs a blank

ImageInputStreamSpi

.

Constructs an

ImageInputStreamSpi

with a given set
of values.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

canUseCacheFile

()

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint.

ImageInputStream

createInputStreamInstance

​(

Object

input)

Returns an instance of the

ImageInputStream

implementation associated with this service provider.

abstract

ImageInputStream

createInputStreamInstance

​(

Object

input,
boolean useCache,

File

cacheDir)

Returns an instance of the

ImageInputStream

implementation associated with this service provider.

Class

<?>

getInputClass

()

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

boolean

needsCacheFile

()

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

.

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

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint.

Returns an instance of the

ImageInputStream

implementation associated with this service provider.

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

.

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

============ FIELD DETAIL ===========

- Field Detail

- inputClass

```java
protected
Class
<?> inputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageInputStreamSpi

```java
protected ImageInputStreamSpi()
```

Constructs a blank

ImageInputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageInputStreamSpi

```java
public ImageInputStreamSpi​(
String
vendorName,

String
version,

Class
<?> inputClass)
```

Constructs an

ImageInputStreamSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** inputClass

- a

Class

object indicating the
legal object type for use by the

createInputStreamInstance

method.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.

============ METHOD DETAIL ==========

- Method Detail

- getInputClass

```java
public
Class
<?> getInputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createInputStreamInstance(Object, boolean, File)

- canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint. If

false

, the value of
the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
input streams created by this service provider.

- needsCacheFile

```java
public boolean needsCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

. If

true

,
the value of the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
input streams created by this service provider.

- createInputStreamInstance

```java
public abstract
ImageInputStream
createInputStreamInstance​(
Object
input,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

,

canUseCacheFile()

,

needsCacheFile()

- createInputStreamInstance

```java
public
ImageInputStream
createInputStreamInstance​(
Object
input)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

Field Detail

- inputClass

```java
protected
Class
<?> inputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

#### Field Detail

inputClass

```java
protected
Class
<?> inputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

#### inputClass

protected

Class

<?> inputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

Constructor Detail

- ImageInputStreamSpi

```java
protected ImageInputStreamSpi()
```

Constructs a blank

ImageInputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageInputStreamSpi

```java
public ImageInputStreamSpi​(
String
vendorName,

String
version,

Class
<?> inputClass)
```

Constructs an

ImageInputStreamSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** inputClass

- a

Class

object indicating the
legal object type for use by the

createInputStreamInstance

method.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.

---

#### Constructor Detail

ImageInputStreamSpi

```java
protected ImageInputStreamSpi()
```

Constructs a blank

ImageInputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### ImageInputStreamSpi

protected ImageInputStreamSpi()

Constructs a blank

ImageInputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

ImageInputStreamSpi

```java
public ImageInputStreamSpi​(
String
vendorName,

String
version,

Class
<?> inputClass)
```

Constructs an

ImageInputStreamSpi

with a given set
of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** inputClass

- a

Class

object indicating the
legal object type for use by the

createInputStreamInstance

method.
**Throws:** IllegalArgumentException

- if

vendorName

is

null

.
**Throws:** IllegalArgumentException

- if

version

is

null

.

---

#### ImageInputStreamSpi

public ImageInputStreamSpi​(

String

vendorName,

String

version,

Class

<?> inputClass)

Constructs an

ImageInputStreamSpi

with a given set
of values.

Method Detail

- getInputClass

```java
public
Class
<?> getInputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createInputStreamInstance(Object, boolean, File)

- canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint. If

false

, the value of
the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
input streams created by this service provider.

- needsCacheFile

```java
public boolean needsCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

. If

true

,
the value of the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
input streams created by this service provider.

- createInputStreamInstance

```java
public abstract
ImageInputStream
createInputStreamInstance​(
Object
input,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

,

canUseCacheFile()

,

needsCacheFile()

- createInputStreamInstance

```java
public
ImageInputStream
createInputStreamInstance​(
Object
input)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

---

#### Method Detail

getInputClass

```java
public
Class
<?> getInputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createInputStreamInstance(Object, boolean, File)

---

#### getInputClass

public

Class

<?> getInputClass()

Returns a

Class

object representing the class or
interface type that must be implemented by an input source in
order to be "wrapped" in an

ImageInputStream

via
the

createInputStreamInstance

method.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

Typical return values might include

InputStream.class

or

URL.class

, but
any class may be used.

canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint. If

false

, the value of
the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
input streams created by this service provider.

---

#### canUseCacheFile

public boolean canUseCacheFile()

Returns

true

if the

ImageInputStream

implementation associated with this service provider can
optionally make use of a cache file for improved performance
and/or memory footrprint. If

false

, the value of
the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

The default implementation returns

false

.

needsCacheFile

```java
public boolean needsCacheFile()
```

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

. If

true

,
the value of the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
input streams created by this service provider.

---

#### needsCacheFile

public boolean needsCacheFile()

Returns

true

if the

ImageInputStream

implementation associated with this service provider requires
the use of a cache

File

. If

true

,
the value of the

useCache

argument to

createInputStreamInstance

will be ignored.

The default implementation returns

false

.

The default implementation returns

false

.

createInputStreamInstance

```java
public abstract
ImageInputStream
createInputStreamInstance​(
Object
input,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Parameters:** useCache

- a

boolean

indicating whether a
cache file should be used, in cases where it is optional.
**Parameters:** cacheDir

- a

File

indicating where the
cache file should be created, or

null

to use the
system directory.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

,

canUseCacheFile()

,

needsCacheFile()

---

#### createInputStreamInstance

public abstract

ImageInputStream

createInputStreamInstance​(

Object

input,
boolean useCache,

File

cacheDir)
throws

IOException

Returns an instance of the

ImageInputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

createInputStreamInstance

```java
public
ImageInputStream
createInputStreamInstance​(
Object
input)
throws
IOException
```

Returns an instance of the

ImageInputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** input

- an object of the class type returned by

getInputClass

.
**Returns:** an

ImageInputStream

instance.
**Throws:** IllegalArgumentException

- if

input

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getInputClass()

---

#### createInputStreamInstance

public

ImageInputStream

createInputStreamInstance​(

Object

input)
throws

IOException

Returns an instance of the

ImageInputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

---

