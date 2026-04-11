# Class ImageOutputStreamSpi

**Source:** `java.desktop\javax\imageio\spi\ImageOutputStreamSpi.html`

### Class Description

```java
public abstract class
ImageOutputStreamSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageOutputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageOutputStream

. For example, a
particular

ImageOutputStreamSpi

might allow a generic

OutputStream

to be used as a destination; another
might output to a

File

or to a device such as a serial
port.

By treating the creation of

ImageOutputStream

s as
a pluggable service, it becomes possible to handle future output
destinations without changing the API. Also, high-performance
implementations of

ImageOutputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

**All Implemented Interfaces:** RegisterableService

---

### Field Details

#### protected
Class
<?> outputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

### Constructor Details

#### protected ImageOutputStreamSpi()

Constructs a blank

ImageOutputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### public ImageOutputStreamSpi​(
String
vendorName,

String
version,

Class
<?> outputClass)

Constructs an

ImageOutputStreamSpi

with a given
set of values.

**Parameters:**
- vendorName

- the vendor name.
- version

- a version identifier.
- outputClass

- a

Class

object indicating the
legal object type for use by the

createOutputStreamInstance

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
<?> getOutputClass()

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

**Returns:**
- a

Class

variable.

**See Also:**
- createOutputStreamInstance(Object, boolean, File)

---

#### public boolean canUseCacheFile()

Returns

true

if the

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint. If

false

,
the value of the

cacheFile

argument to

createOutputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:**
- true

if a cache file can be used by the
output streams created by this service provider.

---

#### public boolean needsCacheFile()

Returns

true

if the

ImageOutputStream

implementation associated with this service provider requires
the use of a cache

File

.

The default implementation returns

false

.

**Returns:**
- true

if a cache file is needed by the
output streams created by this service provider.

---

#### public abstract
ImageOutputStream
createOutputStreamInstance​(
Object
output,
boolean useCache,

File
cacheDir)
throws
IOException

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:**
- output

- an object of the class type returned by

getOutputClass

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

ImageOutputStream

instance.

**Throws:**
- IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
- IllegalArgumentException

- if a cache file is needed,
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
- getOutputClass()

---

#### public
ImageOutputStream
createOutputStreamInstance​(
Object
output)
throws
IOException

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:**
- output

- an object of the class type returned by

getOutputClass

.

**Returns:**
- an

ImageOutputStream

instance.

**Throws:**
- IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
- IOException

- if a cache file is needed but cannot be
created.

**See Also:**
- getOutputClass()

---

### Additional Sections

#### Class ImageOutputStreamSpi

java.lang.Object

- javax.imageio.spi.IIOServiceProvider
- - javax.imageio.spi.ImageOutputStreamSpi

javax.imageio.spi.IIOServiceProvider

- javax.imageio.spi.ImageOutputStreamSpi

javax.imageio.spi.ImageOutputStreamSpi

**All Implemented Interfaces:** RegisterableService

```java
public abstract class
ImageOutputStreamSpi

extends
IIOServiceProvider
```

The service provider interface (SPI) for

ImageOutputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageOutputStream

. For example, a
particular

ImageOutputStreamSpi

might allow a generic

OutputStream

to be used as a destination; another
might output to a

File

or to a device such as a serial
port.

By treating the creation of

ImageOutputStream

s as
a pluggable service, it becomes possible to handle future output
destinations without changing the API. Also, high-performance
implementations of

ImageOutputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

**See Also:** IIORegistry

,

ImageOutputStream

public abstract class

ImageOutputStreamSpi

extends

IIOServiceProvider

The service provider interface (SPI) for

ImageOutputStream

s. For more information on service
provider interfaces, see the class comment for the

IIORegistry

class.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageOutputStream

. For example, a
particular

ImageOutputStreamSpi

might allow a generic

OutputStream

to be used as a destination; another
might output to a

File

or to a device such as a serial
port.

By treating the creation of

ImageOutputStream

s as
a pluggable service, it becomes possible to handle future output
destinations without changing the API. Also, high-performance
implementations of

ImageOutputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

This interface allows arbitrary objects to be "wrapped" by
instances of

ImageOutputStream

. For example, a
particular

ImageOutputStreamSpi

might allow a generic

OutputStream

to be used as a destination; another
might output to a

File

or to a device such as a serial
port.

By treating the creation of

ImageOutputStream

s as
a pluggable service, it becomes possible to handle future output
destinations without changing the API. Also, high-performance
implementations of

ImageOutputStream

(for example,
native implementations for a particular platform) can be installed
and used transparently by applications.

By treating the creation of

ImageOutputStream

s as
a pluggable service, it becomes possible to handle future output
destinations without changing the API. Also, high-performance
implementations of

ImageOutputStream

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

outputClass

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

ImageOutputStreamSpi

()

Constructs a blank

ImageOutputStreamSpi

.

ImageOutputStreamSpi

​(

String

vendorName,

String

version,

Class

<?> outputClass)

Constructs an

ImageOutputStreamSpi

with a given
set of values.

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

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint.

ImageOutputStream

createOutputStreamInstance

​(

Object

output)

Returns an instance of the

ImageOutputStream

implementation associated with this service provider.

abstract

ImageOutputStream

createOutputStreamInstance

​(

Object

output,
boolean useCache,

File

cacheDir)

Returns an instance of the

ImageOutputStream

implementation associated with this service provider.

Class

<?>

getOutputClass

()

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

boolean

needsCacheFile

()

Returns

true

if the

ImageOutputStream

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

outputClass

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

ImageOutputStreamSpi

()

Constructs a blank

ImageOutputStreamSpi

.

ImageOutputStreamSpi

​(

String

vendorName,

String

version,

Class

<?> outputClass)

Constructs an

ImageOutputStreamSpi

with a given
set of values.

---

#### Constructor Summary

Constructs a blank

ImageOutputStreamSpi

.

Constructs an

ImageOutputStreamSpi

with a given
set of values.

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

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint.

ImageOutputStream

createOutputStreamInstance

​(

Object

output)

Returns an instance of the

ImageOutputStream

implementation associated with this service provider.

abstract

ImageOutputStream

createOutputStreamInstance

​(

Object

output,
boolean useCache,

File

cacheDir)

Returns an instance of the

ImageOutputStream

implementation associated with this service provider.

Class

<?>

getOutputClass

()

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

boolean

needsCacheFile

()

Returns

true

if the

ImageOutputStream

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

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint.

Returns an instance of the

ImageOutputStream

implementation associated with this service provider.

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Returns

true

if the

ImageOutputStream

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

- outputClass

```java
protected
Class
<?> outputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ImageOutputStreamSpi

```java
protected ImageOutputStreamSpi()
```

Constructs a blank

ImageOutputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageOutputStreamSpi

```java
public ImageOutputStreamSpi​(
String
vendorName,

String
version,

Class
<?> outputClass)
```

Constructs an

ImageOutputStreamSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** outputClass

- a

Class

object indicating the
legal object type for use by the

createOutputStreamInstance

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

- getOutputClass

```java
public
Class
<?> getOutputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createOutputStreamInstance(Object, boolean, File)

- canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint. If

false

,
the value of the

cacheFile

argument to

createOutputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
output streams created by this service provider.

- needsCacheFile

```java
public boolean needsCacheFile()
```

Returns

true

if the

ImageOutputStream

implementation associated with this service provider requires
the use of a cache

File

.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
output streams created by this service provider.

- createOutputStreamInstance

```java
public abstract
ImageOutputStream
createOutputStreamInstance​(
Object
output,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** output

- an object of the class type returned by

getOutputClass

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

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed,
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

- createOutputStreamInstance

```java
public
ImageOutputStream
createOutputStreamInstance​(
Object
output)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** output

- an object of the class type returned by

getOutputClass

.
**Returns:** an

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

Field Detail

- outputClass

```java
protected
Class
<?> outputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

#### Field Detail

outputClass

```java
protected
Class
<?> outputClass
```

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

---

#### outputClass

protected

Class

<?> outputClass

A

Class

object indicating the legal object type
for use by the

createInputStreamInstance

method.

Constructor Detail

- ImageOutputStreamSpi

```java
protected ImageOutputStreamSpi()
```

Constructs a blank

ImageOutputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

- ImageOutputStreamSpi

```java
public ImageOutputStreamSpi​(
String
vendorName,

String
version,

Class
<?> outputClass)
```

Constructs an

ImageOutputStreamSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** outputClass

- a

Class

object indicating the
legal object type for use by the

createOutputStreamInstance

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

ImageOutputStreamSpi

```java
protected ImageOutputStreamSpi()
```

Constructs a blank

ImageOutputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

---

#### ImageOutputStreamSpi

protected ImageOutputStreamSpi()

Constructs a blank

ImageOutputStreamSpi

. It is up
to the subclass to initialize instance variables and/or
override method implementations in order to provide working
versions of all methods.

ImageOutputStreamSpi

```java
public ImageOutputStreamSpi​(
String
vendorName,

String
version,

Class
<?> outputClass)
```

Constructs an

ImageOutputStreamSpi

with a given
set of values.

**Parameters:** vendorName

- the vendor name.
**Parameters:** version

- a version identifier.
**Parameters:** outputClass

- a

Class

object indicating the
legal object type for use by the

createOutputStreamInstance

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

#### ImageOutputStreamSpi

public ImageOutputStreamSpi​(

String

vendorName,

String

version,

Class

<?> outputClass)

Constructs an

ImageOutputStreamSpi

with a given
set of values.

Method Detail

- getOutputClass

```java
public
Class
<?> getOutputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createOutputStreamInstance(Object, boolean, File)

- canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint. If

false

,
the value of the

cacheFile

argument to

createOutputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
output streams created by this service provider.

- needsCacheFile

```java
public boolean needsCacheFile()
```

Returns

true

if the

ImageOutputStream

implementation associated with this service provider requires
the use of a cache

File

.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
output streams created by this service provider.

- createOutputStreamInstance

```java
public abstract
ImageOutputStream
createOutputStreamInstance​(
Object
output,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** output

- an object of the class type returned by

getOutputClass

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

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed,
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

- createOutputStreamInstance

```java
public
ImageOutputStream
createOutputStreamInstance​(
Object
output)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** output

- an object of the class type returned by

getOutputClass

.
**Returns:** an

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

---

#### Method Detail

getOutputClass

```java
public
Class
<?> getOutputClass()
```

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

**Returns:** a

Class

variable.
**See Also:** createOutputStreamInstance(Object, boolean, File)

---

#### getOutputClass

public

Class

<?> getOutputClass()

Returns a

Class

object representing the class or
interface type that must be implemented by an output
destination in order to be "wrapped" in an

ImageOutputStream

via the

createOutputStreamInstance

method.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

Typical return values might include

OutputStream.class

or

File.class

, but
any class may be used.

canUseCacheFile

```java
public boolean canUseCacheFile()
```

Returns

true

if the

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint. If

false

,
the value of the

cacheFile

argument to

createOutputStreamInstance

will be ignored.

The default implementation returns

false

.

**Returns:** true

if a cache file can be used by the
output streams created by this service provider.

---

#### canUseCacheFile

public boolean canUseCacheFile()

Returns

true

if the

ImageOutputStream

implementation associated with this service provider can
optionally make use of a cache

File

for improved
performance and/or memory footrprint. If

false

,
the value of the

cacheFile

argument to

createOutputStreamInstance

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

ImageOutputStream

implementation associated with this service provider requires
the use of a cache

File

.

The default implementation returns

false

.

**Returns:** true

if a cache file is needed by the
output streams created by this service provider.

---

#### needsCacheFile

public boolean needsCacheFile()

Returns

true

if the

ImageOutputStream

implementation associated with this service provider requires
the use of a cache

File

.

The default implementation returns

false

.

The default implementation returns

false

.

createOutputStreamInstance

```java
public abstract
ImageOutputStream
createOutputStreamInstance​(
Object
output,
boolean useCache,

File
cacheDir)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

**Parameters:** output

- an object of the class type returned by

getOutputClass

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

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IllegalArgumentException

- if a cache file is needed,
but

cacheDir

is non-

null

and is not a
directory.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

---

#### createOutputStreamInstance

public abstract

ImageOutputStream

createOutputStreamInstance​(

Object

output,
boolean useCache,

File

cacheDir)
throws

IOException

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. If the
use of a cache file is optional, the

useCache

parameter will be consulted. Where a cache is required, or
not applicable, the value of

useCache

will be ignored.

createOutputStreamInstance

```java
public
ImageOutputStream
createOutputStreamInstance​(
Object
output)
throws
IOException
```

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

**Parameters:** output

- an object of the class type returned by

getOutputClass

.
**Returns:** an

ImageOutputStream

instance.
**Throws:** IllegalArgumentException

- if

output

is
not an instance of the correct class or is

null

.
**Throws:** IOException

- if a cache file is needed but cannot be
created.
**See Also:** getOutputClass()

---

#### createOutputStreamInstance

public

ImageOutputStream

createOutputStreamInstance​(

Object

output)
throws

IOException

Returns an instance of the

ImageOutputStream

implementation associated with this service provider. A cache
file will be created in the system-dependent default
temporary-file directory, if needed.

---

