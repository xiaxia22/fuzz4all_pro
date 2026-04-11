# Class PrintServiceLookup

**Source:** `java.desktop\javax\print\PrintServiceLookup.html`

### Class Description

```java
public abstract class
PrintServiceLookup

extends
Object
```

Implementations of this class provide lookup services for print services
(typically equivalent to printers) of a particular type.

Multiple implementations may be installed concurrently. All implementations
must be able to describe the located printers as instances of a

PrintService

. Typically implementations of this service class are
located automatically in JAR files (see the SPI JAR file specification).
These classes must be instantiable using a default constructor. Alternatively
applications may explicitly register instances at runtime.

Applications use only the static methods of this abstract class. The instance
methods are implemented by a service provider in a subclass and the
unification of the results from all installed lookup classes are reported by
the static methods of this class when called by the application.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrintServiceLookup()

*No description found.*

---

### Method Details

#### public static final
PrintService
[] lookupPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)

Locates print services capable of printing the specified

DocFlavor

.

**Parameters:**
- flavor

- the flavor to print. If

null

, this constraint is
not used.
- attributes

- attributes that the print service must support. If

null

this constraint is not used.

**Returns:**
- array of matching

PrintService

objects representing print
services that support the specified flavor attributes. If no
services match, the array is zero-length.

---

#### public static final
MultiDocPrintService
[] lookupMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

**Parameters:**
- flavors

- the flavors to print. If

null

or empty this
constraint is not used. Otherwise return only multidoc print
services that can print all specified doc flavors.
- attributes

- attributes that the print service must support. If

null

this constraint is not used.

**Returns:**
- array of matching

MultiDocPrintService

objects. If no
services match, the array is zero-length.

---

#### public static final
PrintService
lookupDefaultPrintService()

Locates the default print service for this environment. This may return

null

. If multiple lookup services each specify a default, the
chosen service is not precisely defined, but a platform native service,
rather than an installed service, is usually returned as the default. If
there is no clearly identifiable platform native default print service,
the default is the first to be located in an implementation-dependent
manner.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

**Returns:**
- the default

PrintService

---

#### public static boolean registerServiceProvider​(
PrintServiceLookup
sp)

Allows an application to explicitly register a class that implements
lookup services. The registration will not persist across VM invocations.
This is useful if an application needs to make a new service available
that is not part of the installation. If the lookup service is already
registered, or cannot be registered, the method returns

false

.

**Parameters:**
- sp

- an implementation of a lookup service

**Returns:**
- true

if the new lookup service is newly registered;

false

otherwise

---

#### public static boolean registerService​(
PrintService
service)

Allows an application to directly register an instance of a class which
implements a print service. The lookup operations for this service will
be performed by the

PrintServiceLookup

class using the attribute
values and classes reported by the service. This may be less efficient
than a lookup service tuned for that service. Therefore registering a

PrintServiceLookup

instance instead is recommended. The method
returns

true

if this service is not previously registered and is
now successfully registered. This method should not be called with

StreamPrintService

instances. They will always fail to register
and the method will return

false

.

**Parameters:**
- service

- an implementation of a print service

**Returns:**
- true

if the service is newly registered;

false

otherwise

---

#### public abstract
PrintService
[] getPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified. This method
is not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

**Parameters:**
- flavor

- of document required. If

null

it is ignored.
- attributes

- required to be supported. If

null

this
constraint is not used.

**Returns:**
- array of matching

PrintServices

. If no services match,
the array is zero-length.

---

#### public abstract
PrintService
[] getPrintServices()

Not called directly by applications. Implemented by a service provider,
used by the static methods of this class.

**Returns:**
- array of all

PrintServices

known to this lookup service
class. If none are found, the array is zero-length.

---

#### public abstract
MultiDocPrintService
[] getMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)

Not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

**Parameters:**
- flavors

- of documents required. If

null

or empty it is
ignored.
- attributes

- required to be supported. If

null

this
constraint is not used.

**Returns:**
- array of matching

PrintServices

. If no services match,
the array is zero-length.

---

#### public abstract
PrintService
getDefaultPrintService()

Not called directly by applications. Implemented by a service provider,
and called by the print lookup service.

**Returns:**
- the default

PrintService

for this lookup service. If
there is no default, returns

null

.

---

### Additional Sections

#### Class PrintServiceLookup

java.lang.Object

- javax.print.PrintServiceLookup

javax.print.PrintServiceLookup

```java
public abstract class
PrintServiceLookup

extends
Object
```

Implementations of this class provide lookup services for print services
(typically equivalent to printers) of a particular type.

Multiple implementations may be installed concurrently. All implementations
must be able to describe the located printers as instances of a

PrintService

. Typically implementations of this service class are
located automatically in JAR files (see the SPI JAR file specification).
These classes must be instantiable using a default constructor. Alternatively
applications may explicitly register instances at runtime.

Applications use only the static methods of this abstract class. The instance
methods are implemented by a service provider in a subclass and the
unification of the results from all installed lookup classes are reported by
the static methods of this class when called by the application.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

public abstract class

PrintServiceLookup

extends

Object

Implementations of this class provide lookup services for print services
(typically equivalent to printers) of a particular type.

Multiple implementations may be installed concurrently. All implementations
must be able to describe the located printers as instances of a

PrintService

. Typically implementations of this service class are
located automatically in JAR files (see the SPI JAR file specification).
These classes must be instantiable using a default constructor. Alternatively
applications may explicitly register instances at runtime.

Applications use only the static methods of this abstract class. The instance
methods are implemented by a service provider in a subclass and the
unification of the results from all installed lookup classes are reported by
the static methods of this class when called by the application.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

Multiple implementations may be installed concurrently. All implementations
must be able to describe the located printers as instances of a

PrintService

. Typically implementations of this service class are
located automatically in JAR files (see the SPI JAR file specification).
These classes must be instantiable using a default constructor. Alternatively
applications may explicitly register instances at runtime.

Applications use only the static methods of this abstract class. The instance
methods are implemented by a service provider in a subclass and the
unification of the results from all installed lookup classes are reported by
the static methods of this class when called by the application.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

Applications use only the static methods of this abstract class. The instance
methods are implemented by a service provider in a subclass and the
unification of the results from all installed lookup classes are reported by
the static methods of this class when called by the application.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

A

PrintServiceLookup

implementor is recommended to check for the

SecurityManager.checkPrintJobAccess()

to deny access to untrusted
code. Following this recommended policy means that untrusted code may not be
able to locate any print services. Downloaded applets are the most common
example of untrusted code.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

This check is made on a per lookup service basis to allow flexibility in the
policy to reflect the needs of different lookup services.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

Services which are registered by

registerService(PrintService)

will
not be included in lookup results if a security manager is installed and its

checkPrintJobAccess()

method denies access.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrintServiceLookup

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

PrintService

getDefaultPrintService

()

Not called directly by applications.

abstract

MultiDocPrintService

[]

getMultiDocPrintServices

​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Not called directly by applications.

abstract

PrintService

[]

getPrintServices

()

Not called directly by applications.

abstract

PrintService

[]

getPrintServices

​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified.

static

PrintService

lookupDefaultPrintService

()

Locates the default print service for this environment.

static

MultiDocPrintService

[]

lookupMultiDocPrintServices

​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

static

PrintService

[]

lookupPrintServices

​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates print services capable of printing the specified

DocFlavor

.

static boolean

registerService

​(

PrintService

service)

Allows an application to directly register an instance of a class which
implements a print service.

static boolean

registerServiceProvider

​(

PrintServiceLookup

sp)

Allows an application to explicitly register a class that implements
lookup services.

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

Constructor Summary

Constructors

Constructor

Description

PrintServiceLookup

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

PrintService

getDefaultPrintService

()

Not called directly by applications.

abstract

MultiDocPrintService

[]

getMultiDocPrintServices

​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Not called directly by applications.

abstract

PrintService

[]

getPrintServices

()

Not called directly by applications.

abstract

PrintService

[]

getPrintServices

​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified.

static

PrintService

lookupDefaultPrintService

()

Locates the default print service for this environment.

static

MultiDocPrintService

[]

lookupMultiDocPrintServices

​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

static

PrintService

[]

lookupPrintServices

​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates print services capable of printing the specified

DocFlavor

.

static boolean

registerService

​(

PrintService

service)

Allows an application to directly register an instance of a class which
implements a print service.

static boolean

registerServiceProvider

​(

PrintServiceLookup

sp)

Allows an application to explicitly register a class that implements
lookup services.

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

Not called directly by applications.

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified.

Locates the default print service for this environment.

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

Locates print services capable of printing the specified

DocFlavor

.

Allows an application to directly register an instance of a class which
implements a print service.

Allows an application to explicitly register a class that implements
lookup services.

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

- PrintServiceLookup

```java
public PrintServiceLookup()
```

============ METHOD DETAIL ==========

- Method Detail

- lookupPrintServices

```java
public static final
PrintService
[] lookupPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates print services capable of printing the specified

DocFlavor

.

**Parameters:** flavor

- the flavor to print. If

null

, this constraint is
not used.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

PrintService

objects representing print
services that support the specified flavor attributes. If no
services match, the array is zero-length.

- lookupMultiDocPrintServices

```java
public static final
MultiDocPrintService
[] lookupMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

**Parameters:** flavors

- the flavors to print. If

null

or empty this
constraint is not used. Otherwise return only multidoc print
services that can print all specified doc flavors.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

MultiDocPrintService

objects. If no
services match, the array is zero-length.

- lookupDefaultPrintService

```java
public static final
PrintService
lookupDefaultPrintService()
```

Locates the default print service for this environment. This may return

null

. If multiple lookup services each specify a default, the
chosen service is not precisely defined, but a platform native service,
rather than an installed service, is usually returned as the default. If
there is no clearly identifiable platform native default print service,
the default is the first to be located in an implementation-dependent
manner.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

**Returns:** the default

PrintService

- registerServiceProvider

```java
public static boolean registerServiceProvider​(
PrintServiceLookup
sp)
```

Allows an application to explicitly register a class that implements
lookup services. The registration will not persist across VM invocations.
This is useful if an application needs to make a new service available
that is not part of the installation. If the lookup service is already
registered, or cannot be registered, the method returns

false

.

**Parameters:** sp

- an implementation of a lookup service
**Returns:** true

if the new lookup service is newly registered;

false

otherwise

- registerService

```java
public static boolean registerService​(
PrintService
service)
```

Allows an application to directly register an instance of a class which
implements a print service. The lookup operations for this service will
be performed by the

PrintServiceLookup

class using the attribute
values and classes reported by the service. This may be less efficient
than a lookup service tuned for that service. Therefore registering a

PrintServiceLookup

instance instead is recommended. The method
returns

true

if this service is not previously registered and is
now successfully registered. This method should not be called with

StreamPrintService

instances. They will always fail to register
and the method will return

false

.

**Parameters:** service

- an implementation of a print service
**Returns:** true

if the service is newly registered;

false

otherwise

- getPrintServices

```java
public abstract
PrintService
[] getPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified. This method
is not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

**Parameters:** flavor

- of document required. If

null

it is ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

- getPrintServices

```java
public abstract
PrintService
[] getPrintServices()
```

Not called directly by applications. Implemented by a service provider,
used by the static methods of this class.

**Returns:** array of all

PrintServices

known to this lookup service
class. If none are found, the array is zero-length.

- getMultiDocPrintServices

```java
public abstract
MultiDocPrintService
[] getMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

**Parameters:** flavors

- of documents required. If

null

or empty it is
ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

- getDefaultPrintService

```java
public abstract
PrintService
getDefaultPrintService()
```

Not called directly by applications. Implemented by a service provider,
and called by the print lookup service.

**Returns:** the default

PrintService

for this lookup service. If
there is no default, returns

null

.

Constructor Detail

- PrintServiceLookup

```java
public PrintServiceLookup()
```

---

#### Constructor Detail

PrintServiceLookup

```java
public PrintServiceLookup()
```

---

#### PrintServiceLookup

public PrintServiceLookup()

Method Detail

- lookupPrintServices

```java
public static final
PrintService
[] lookupPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates print services capable of printing the specified

DocFlavor

.

**Parameters:** flavor

- the flavor to print. If

null

, this constraint is
not used.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

PrintService

objects representing print
services that support the specified flavor attributes. If no
services match, the array is zero-length.

- lookupMultiDocPrintServices

```java
public static final
MultiDocPrintService
[] lookupMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

**Parameters:** flavors

- the flavors to print. If

null

or empty this
constraint is not used. Otherwise return only multidoc print
services that can print all specified doc flavors.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

MultiDocPrintService

objects. If no
services match, the array is zero-length.

- lookupDefaultPrintService

```java
public static final
PrintService
lookupDefaultPrintService()
```

Locates the default print service for this environment. This may return

null

. If multiple lookup services each specify a default, the
chosen service is not precisely defined, but a platform native service,
rather than an installed service, is usually returned as the default. If
there is no clearly identifiable platform native default print service,
the default is the first to be located in an implementation-dependent
manner.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

**Returns:** the default

PrintService

- registerServiceProvider

```java
public static boolean registerServiceProvider​(
PrintServiceLookup
sp)
```

Allows an application to explicitly register a class that implements
lookup services. The registration will not persist across VM invocations.
This is useful if an application needs to make a new service available
that is not part of the installation. If the lookup service is already
registered, or cannot be registered, the method returns

false

.

**Parameters:** sp

- an implementation of a lookup service
**Returns:** true

if the new lookup service is newly registered;

false

otherwise

- registerService

```java
public static boolean registerService​(
PrintService
service)
```

Allows an application to directly register an instance of a class which
implements a print service. The lookup operations for this service will
be performed by the

PrintServiceLookup

class using the attribute
values and classes reported by the service. This may be less efficient
than a lookup service tuned for that service. Therefore registering a

PrintServiceLookup

instance instead is recommended. The method
returns

true

if this service is not previously registered and is
now successfully registered. This method should not be called with

StreamPrintService

instances. They will always fail to register
and the method will return

false

.

**Parameters:** service

- an implementation of a print service
**Returns:** true

if the service is newly registered;

false

otherwise

- getPrintServices

```java
public abstract
PrintService
[] getPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified. This method
is not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

**Parameters:** flavor

- of document required. If

null

it is ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

- getPrintServices

```java
public abstract
PrintService
[] getPrintServices()
```

Not called directly by applications. Implemented by a service provider,
used by the static methods of this class.

**Returns:** array of all

PrintServices

known to this lookup service
class. If none are found, the array is zero-length.

- getMultiDocPrintServices

```java
public abstract
MultiDocPrintService
[] getMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

**Parameters:** flavors

- of documents required. If

null

or empty it is
ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

- getDefaultPrintService

```java
public abstract
PrintService
getDefaultPrintService()
```

Not called directly by applications. Implemented by a service provider,
and called by the print lookup service.

**Returns:** the default

PrintService

for this lookup service. If
there is no default, returns

null

.

---

#### Method Detail

lookupPrintServices

```java
public static final
PrintService
[] lookupPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates print services capable of printing the specified

DocFlavor

.

**Parameters:** flavor

- the flavor to print. If

null

, this constraint is
not used.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

PrintService

objects representing print
services that support the specified flavor attributes. If no
services match, the array is zero-length.

---

#### lookupPrintServices

public static final

PrintService

[] lookupPrintServices​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates print services capable of printing the specified

DocFlavor

.

lookupMultiDocPrintServices

```java
public static final
MultiDocPrintService
[] lookupMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

**Parameters:** flavors

- the flavors to print. If

null

or empty this
constraint is not used. Otherwise return only multidoc print
services that can print all specified doc flavors.
**Parameters:** attributes

- attributes that the print service must support. If

null

this constraint is not used.
**Returns:** array of matching

MultiDocPrintService

objects. If no
services match, the array is zero-length.

---

#### lookupMultiDocPrintServices

public static final

MultiDocPrintService

[] lookupMultiDocPrintServices​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Locates

MultiDoc

print

Services

capable of printing

MultiDocs

containing all the specified doc flavors.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

This method is useful to help locate a service that can print a

MultiDoc

in which the elements may be different flavors. An
application could perform this itself by multiple lookups on each

DocFlavor

in turn and collating the results, but the lookup
service may be able to do this more efficiently.

lookupDefaultPrintService

```java
public static final
PrintService
lookupDefaultPrintService()
```

Locates the default print service for this environment. This may return

null

. If multiple lookup services each specify a default, the
chosen service is not precisely defined, but a platform native service,
rather than an installed service, is usually returned as the default. If
there is no clearly identifiable platform native default print service,
the default is the first to be located in an implementation-dependent
manner.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

**Returns:** the default

PrintService

---

#### lookupDefaultPrintService

public static final

PrintService

lookupDefaultPrintService()

Locates the default print service for this environment. This may return

null

. If multiple lookup services each specify a default, the
chosen service is not precisely defined, but a platform native service,
rather than an installed service, is usually returned as the default. If
there is no clearly identifiable platform native default print service,
the default is the first to be located in an implementation-dependent
manner.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

This may include making use of any preferences API that is available as
part of the Java or native platform. This algorithm may be overridden by
a user setting the property

javax.print.defaultPrinter

. A service
specified must be discovered to be valid and currently available to be
returned as the default.

registerServiceProvider

```java
public static boolean registerServiceProvider​(
PrintServiceLookup
sp)
```

Allows an application to explicitly register a class that implements
lookup services. The registration will not persist across VM invocations.
This is useful if an application needs to make a new service available
that is not part of the installation. If the lookup service is already
registered, or cannot be registered, the method returns

false

.

**Parameters:** sp

- an implementation of a lookup service
**Returns:** true

if the new lookup service is newly registered;

false

otherwise

---

#### registerServiceProvider

public static boolean registerServiceProvider​(

PrintServiceLookup

sp)

Allows an application to explicitly register a class that implements
lookup services. The registration will not persist across VM invocations.
This is useful if an application needs to make a new service available
that is not part of the installation. If the lookup service is already
registered, or cannot be registered, the method returns

false

.

registerService

```java
public static boolean registerService​(
PrintService
service)
```

Allows an application to directly register an instance of a class which
implements a print service. The lookup operations for this service will
be performed by the

PrintServiceLookup

class using the attribute
values and classes reported by the service. This may be less efficient
than a lookup service tuned for that service. Therefore registering a

PrintServiceLookup

instance instead is recommended. The method
returns

true

if this service is not previously registered and is
now successfully registered. This method should not be called with

StreamPrintService

instances. They will always fail to register
and the method will return

false

.

**Parameters:** service

- an implementation of a print service
**Returns:** true

if the service is newly registered;

false

otherwise

---

#### registerService

public static boolean registerService​(

PrintService

service)

Allows an application to directly register an instance of a class which
implements a print service. The lookup operations for this service will
be performed by the

PrintServiceLookup

class using the attribute
values and classes reported by the service. This may be less efficient
than a lookup service tuned for that service. Therefore registering a

PrintServiceLookup

instance instead is recommended. The method
returns

true

if this service is not previously registered and is
now successfully registered. This method should not be called with

StreamPrintService

instances. They will always fail to register
and the method will return

false

.

getPrintServices

```java
public abstract
PrintService
[] getPrintServices​(
DocFlavor
flavor,

AttributeSet
attributes)
```

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified. This method
is not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

**Parameters:** flavor

- of document required. If

null

it is ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

---

#### getPrintServices

public abstract

PrintService

[] getPrintServices​(

DocFlavor

flavor,

AttributeSet

attributes)

Locates services that can be positively confirmed to support the
combination of attributes and

DocFlavors

specified. This method
is not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

Implemented by a service provider, used by the static methods of this
class.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

The results should be the same as obtaining all the

PrintServices

and querying each one individually on its support for the specified
attributes and flavors, but the process can be more efficient by taking
advantage of the capabilities of lookup services for the print services.

getPrintServices

```java
public abstract
PrintService
[] getPrintServices()
```

Not called directly by applications. Implemented by a service provider,
used by the static methods of this class.

**Returns:** array of all

PrintServices

known to this lookup service
class. If none are found, the array is zero-length.

---

#### getPrintServices

public abstract

PrintService

[] getPrintServices()

Not called directly by applications. Implemented by a service provider,
used by the static methods of this class.

getMultiDocPrintServices

```java
public abstract
MultiDocPrintService
[] getMultiDocPrintServices​(
DocFlavor
[] flavors,

AttributeSet
attributes)
```

Not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

**Parameters:** flavors

- of documents required. If

null

or empty it is
ignored.
**Parameters:** attributes

- required to be supported. If

null

this
constraint is not used.
**Returns:** array of matching

PrintServices

. If no services match,
the array is zero-length.

---

#### getMultiDocPrintServices

public abstract

MultiDocPrintService

[] getMultiDocPrintServices​(

DocFlavor

[] flavors,

AttributeSet

attributes)

Not called directly by applications.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

Implemented by a service provider, used by the static methods of this
class.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

Locates

MultiDoc

print services which can be positively confirmed
to support the combination of attributes and

DocFlavors

specified.

getDefaultPrintService

```java
public abstract
PrintService
getDefaultPrintService()
```

Not called directly by applications. Implemented by a service provider,
and called by the print lookup service.

**Returns:** the default

PrintService

for this lookup service. If
there is no default, returns

null

.

---

#### getDefaultPrintService

public abstract

PrintService

getDefaultPrintService()

Not called directly by applications. Implemented by a service provider,
and called by the print lookup service.

---

