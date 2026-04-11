# Class AbstractResourceBundleProvider

**Source:** `java.base\java\util\spi\AbstractResourceBundleProvider.html`

### Class Description

```java
public abstract class
AbstractResourceBundleProvider

extends
Object

implements
ResourceBundleProvider
```

AbstractResourceBundleProvider

is an abstract class that provides
the basic support for a provider implementation class for

ResourceBundleProvider

.

Resource bundles can be packaged in one or more
named modules,

service provider modules

. The

consumer

of the
resource bundle is the one calling

ResourceBundle.getBundle(String)

.
In order for the consumer module to load a resource bundle
"

com.example.app.MyResources

" provided by another module,
it will use the

service loader

mechanism. A service interface named "

com.example.app.spi.MyResourcesProvider

"
must be defined and a

service provider module

will provide an
implementation class of "

com.example.app.spi.MyResourcesProvider

"
as follows:

```java
import com.example.app.spi.MyResourcesProvider;
class MyResourcesProviderImpl extends AbstractResourceBundleProvider
implements MyResourcesProvider
{
public MyResourcesProviderImpl() {
super("java.properties");
}
// this provider maps the resource bundle to per-language package
protected String toBundleName(String baseName, Locale locale) {
return "p." + locale.getLanguage() + "." + baseName;
}

public ResourceBundle getBundle(String baseName, Locale locale) {
// this module only provides bundles in French
if (locale.equals(Locale.FRENCH)) {
return super.getBundle(baseName, locale);
}
// otherwise return null
return null;
}
}
```

Refer to

ResourceBundleProvider

for details.

**All Implemented Interfaces:** ResourceBundleProvider

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractResourceBundleProvider()

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format. This constructor is equivalent to

AbstractResourceBundleProvider("java.properties")

.

---

#### protected AbstractResourceBundleProvider​(
String
... formats)

Constructs an

AbstractResourceBundleProvider

with the specified

formats

. The

getBundle(String, Locale)

method looks up
resource bundles for the given

formats

.

formats

must
be "java.class" or "java.properties".

**Parameters:**
- formats

- the formats to be used for loading resource bundles

**Throws:**
- NullPointerException

- if the given

formats

is null
- IllegalArgumentException

- if the given

formats

is not
"java.class" or "java.properties".

---

### Method Details

#### protected
String
toBundleName​(
String
baseName,

Locale
locale)

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

**Parameters:**
- baseName

- the base name of the resource bundle, a fully qualified
class name
- locale

- the locale for which a resource bundle should be loaded

**Returns:**
- the bundle name for the resource bundle

**API Note:**
- A resource bundle provider may package its resource bundles in the
same package as the base name of the resource bundle if the package
is not split among other named modules. If there are more than one
bundle providers providing the resource bundle of a given base name,
the resource bundles can be packaged with per-language grouping
or per-region grouping to eliminate the split packages.

For example, if

baseName

is

"p.resources.Bundle"

then
the resource bundle name of

"p.resources.Bundle"

of

Locale("ja", "", "XX")

and

Locale("en")

could be

"p.resources.ja.Bundle_ja_ _XX"

and

"p.resources.Bundle_en"

respectively.

This method is called from the default implementation of the

getBundle(String, Locale)

method.

**Implementation Note:**
- The default implementation of this method is the same as the
implementation of

ResourceBundle.Control.toBundleName(String, Locale)

.

---

#### public
ResourceBundle
getBundle​(
String
baseName,

Locale
locale)

Returns a

ResourceBundle

for the given

baseName

and

locale

.

**Specified by:**
- getBundle

in interface

ResourceBundleProvider

**Parameters:**
- baseName

- the base bundle name of the resource bundle, a fully
qualified class name.
- locale

- the locale for which the resource bundle should be instantiated

**Returns:**
- ResourceBundle

of the given

baseName

and

locale

, or

null

if no resource bundle is found

**Throws:**
- NullPointerException

- if

baseName

or

locale

is

null
- UncheckedIOException

- if any IO exception occurred during resource
bundle loading

**Implementation Note:**
- The default implementation of this method calls the

toBundleName

method to get the
bundle name for the

baseName

and

locale

and finds the
resource bundle of the bundle name local in the module of this provider.
It will only search the formats specified when this provider was
constructed.

---

### Additional Sections

#### Class AbstractResourceBundleProvider

java.lang.Object

- java.util.spi.AbstractResourceBundleProvider

java.util.spi.AbstractResourceBundleProvider

**All Implemented Interfaces:** ResourceBundleProvider

```java
public abstract class
AbstractResourceBundleProvider

extends
Object

implements
ResourceBundleProvider
```

AbstractResourceBundleProvider

is an abstract class that provides
the basic support for a provider implementation class for

ResourceBundleProvider

.

Resource bundles can be packaged in one or more
named modules,

service provider modules

. The

consumer

of the
resource bundle is the one calling

ResourceBundle.getBundle(String)

.
In order for the consumer module to load a resource bundle
"

com.example.app.MyResources

" provided by another module,
it will use the

service loader

mechanism. A service interface named "

com.example.app.spi.MyResourcesProvider

"
must be defined and a

service provider module

will provide an
implementation class of "

com.example.app.spi.MyResourcesProvider

"
as follows:

```java
import com.example.app.spi.MyResourcesProvider;
class MyResourcesProviderImpl extends AbstractResourceBundleProvider
implements MyResourcesProvider
{
public MyResourcesProviderImpl() {
super("java.properties");
}
// this provider maps the resource bundle to per-language package
protected String toBundleName(String baseName, Locale locale) {
return "p." + locale.getLanguage() + "." + baseName;
}

public ResourceBundle getBundle(String baseName, Locale locale) {
// this module only provides bundles in French
if (locale.equals(Locale.FRENCH)) {
return super.getBundle(baseName, locale);
}
// otherwise return null
return null;
}
}
```

Refer to

ResourceBundleProvider

for details.

**Since:** 9
**See Also:** Resource Bundles and Named Modules

public abstract class

AbstractResourceBundleProvider

extends

Object

implements

ResourceBundleProvider

AbstractResourceBundleProvider

is an abstract class that provides
the basic support for a provider implementation class for

ResourceBundleProvider

.

Resource bundles can be packaged in one or more
named modules,

service provider modules

. The

consumer

of the
resource bundle is the one calling

ResourceBundle.getBundle(String)

.
In order for the consumer module to load a resource bundle
"

com.example.app.MyResources

" provided by another module,
it will use the

service loader

mechanism. A service interface named "

com.example.app.spi.MyResourcesProvider

"
must be defined and a

service provider module

will provide an
implementation class of "

com.example.app.spi.MyResourcesProvider

"
as follows:

```java
import com.example.app.spi.MyResourcesProvider;
class MyResourcesProviderImpl extends AbstractResourceBundleProvider
implements MyResourcesProvider
{
public MyResourcesProviderImpl() {
super("java.properties");
}
// this provider maps the resource bundle to per-language package
protected String toBundleName(String baseName, Locale locale) {
return "p." + locale.getLanguage() + "." + baseName;
}

public ResourceBundle getBundle(String baseName, Locale locale) {
// this module only provides bundles in French
if (locale.equals(Locale.FRENCH)) {
return super.getBundle(baseName, locale);
}
// otherwise return null
return null;
}
}
```

Refer to

ResourceBundleProvider

for details.

Resource bundles can be packaged in one or more
named modules,

service provider modules

. The

consumer

of the
resource bundle is the one calling

ResourceBundle.getBundle(String)

.
In order for the consumer module to load a resource bundle
"

com.example.app.MyResources

" provided by another module,
it will use the

service loader

mechanism. A service interface named "

com.example.app.spi.MyResourcesProvider

"
must be defined and a

service provider module

will provide an
implementation class of "

com.example.app.spi.MyResourcesProvider

"
as follows:

```java
import com.example.app.spi.MyResourcesProvider;
class MyResourcesProviderImpl extends AbstractResourceBundleProvider
implements MyResourcesProvider
{
public MyResourcesProviderImpl() {
super("java.properties");
}
// this provider maps the resource bundle to per-language package
protected String toBundleName(String baseName, Locale locale) {
return "p." + locale.getLanguage() + "." + baseName;
}

public ResourceBundle getBundle(String baseName, Locale locale) {
// this module only provides bundles in French
if (locale.equals(Locale.FRENCH)) {
return super.getBundle(baseName, locale);
}
// otherwise return null
return null;
}
}
```

Refer to

ResourceBundleProvider

for details.

import com.example.app.spi.MyResourcesProvider;
class MyResourcesProviderImpl extends AbstractResourceBundleProvider
implements MyResourcesProvider
{
public MyResourcesProviderImpl() {
super("java.properties");
}
// this provider maps the resource bundle to per-language package
protected String toBundleName(String baseName, Locale locale) {
return "p." + locale.getLanguage() + "." + baseName;
}

public ResourceBundle getBundle(String baseName, Locale locale) {
// this module only provides bundles in French
if (locale.equals(Locale.FRENCH)) {
return super.getBundle(baseName, locale);
}
// otherwise return null
return null;
}
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractResourceBundleProvider

()

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format.

protected

AbstractResourceBundleProvider

​(

String

... formats)

Constructs an

AbstractResourceBundleProvider

with the specified

formats

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ResourceBundle

getBundle

​(

String

baseName,

Locale

locale)

Returns a

ResourceBundle

for the given

baseName

and

locale

.

protected

String

toBundleName

​(

String

baseName,

Locale

locale)

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

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

Modifier

Constructor

Description

protected

AbstractResourceBundleProvider

()

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format.

protected

AbstractResourceBundleProvider

​(

String

... formats)

Constructs an

AbstractResourceBundleProvider

with the specified

formats

.

---

#### Constructor Summary

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format.

Constructs an

AbstractResourceBundleProvider

with the specified

formats

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ResourceBundle

getBundle

​(

String

baseName,

Locale

locale)

Returns a

ResourceBundle

for the given

baseName

and

locale

.

protected

String

toBundleName

​(

String

baseName,

Locale

locale)

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

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

Returns a

ResourceBundle

for the given

baseName

and

locale

.

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

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

- AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider()
```

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format. This constructor is equivalent to

AbstractResourceBundleProvider("java.properties")

.

- AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider​(
String
... formats)
```

Constructs an

AbstractResourceBundleProvider

with the specified

formats

. The

getBundle(String, Locale)

method looks up
resource bundles for the given

formats

.

formats

must
be "java.class" or "java.properties".

**Parameters:** formats

- the formats to be used for loading resource bundles
**Throws:** NullPointerException

- if the given

formats

is null
**Throws:** IllegalArgumentException

- if the given

formats

is not
"java.class" or "java.properties".

============ METHOD DETAIL ==========

- Method Detail

- toBundleName

```java
protected
String
toBundleName​(
String
baseName,

Locale
locale)
```

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

**API Note:** A resource bundle provider may package its resource bundles in the
same package as the base name of the resource bundle if the package
is not split among other named modules. If there are more than one
bundle providers providing the resource bundle of a given base name,
the resource bundles can be packaged with per-language grouping
or per-region grouping to eliminate the split packages.

For example, if

baseName

is

"p.resources.Bundle"

then
the resource bundle name of

"p.resources.Bundle"

of

Locale("ja", "", "XX")

and

Locale("en")

could be

"p.resources.ja.Bundle_ja_ _XX"

and

"p.resources.Bundle_en"

respectively.

This method is called from the default implementation of the

getBundle(String, Locale)

method.
**Implementation Note:** The default implementation of this method is the same as the
implementation of

ResourceBundle.Control.toBundleName(String, Locale)

.
**Parameters:** baseName

- the base name of the resource bundle, a fully qualified
class name
**Parameters:** locale

- the locale for which a resource bundle should be loaded
**Returns:** the bundle name for the resource bundle

- getBundle

```java
public
ResourceBundle
getBundle​(
String
baseName,

Locale
locale)
```

Returns a

ResourceBundle

for the given

baseName

and

locale

.

**Specified by:** getBundle

in interface

ResourceBundleProvider
**Implementation Note:** The default implementation of this method calls the

toBundleName

method to get the
bundle name for the

baseName

and

locale

and finds the
resource bundle of the bundle name local in the module of this provider.
It will only search the formats specified when this provider was
constructed.
**Parameters:** baseName

- the base bundle name of the resource bundle, a fully
qualified class name.
**Parameters:** locale

- the locale for which the resource bundle should be instantiated
**Returns:** ResourceBundle

of the given

baseName

and

locale

, or

null

if no resource bundle is found
**Throws:** NullPointerException

- if

baseName

or

locale

is

null
**Throws:** UncheckedIOException

- if any IO exception occurred during resource
bundle loading

Constructor Detail

- AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider()
```

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format. This constructor is equivalent to

AbstractResourceBundleProvider("java.properties")

.

- AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider​(
String
... formats)
```

Constructs an

AbstractResourceBundleProvider

with the specified

formats

. The

getBundle(String, Locale)

method looks up
resource bundles for the given

formats

.

formats

must
be "java.class" or "java.properties".

**Parameters:** formats

- the formats to be used for loading resource bundles
**Throws:** NullPointerException

- if the given

formats

is null
**Throws:** IllegalArgumentException

- if the given

formats

is not
"java.class" or "java.properties".

---

#### Constructor Detail

AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider()
```

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format. This constructor is equivalent to

AbstractResourceBundleProvider("java.properties")

.

---

#### AbstractResourceBundleProvider

protected AbstractResourceBundleProvider()

Constructs an

AbstractResourceBundleProvider

with the
"java.properties" format. This constructor is equivalent to

AbstractResourceBundleProvider("java.properties")

.

AbstractResourceBundleProvider

```java
protected AbstractResourceBundleProvider​(
String
... formats)
```

Constructs an

AbstractResourceBundleProvider

with the specified

formats

. The

getBundle(String, Locale)

method looks up
resource bundles for the given

formats

.

formats

must
be "java.class" or "java.properties".

**Parameters:** formats

- the formats to be used for loading resource bundles
**Throws:** NullPointerException

- if the given

formats

is null
**Throws:** IllegalArgumentException

- if the given

formats

is not
"java.class" or "java.properties".

---

#### AbstractResourceBundleProvider

protected AbstractResourceBundleProvider​(

String

... formats)

Constructs an

AbstractResourceBundleProvider

with the specified

formats

. The

getBundle(String, Locale)

method looks up
resource bundles for the given

formats

.

formats

must
be "java.class" or "java.properties".

Method Detail

- toBundleName

```java
protected
String
toBundleName​(
String
baseName,

Locale
locale)
```

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

**API Note:** A resource bundle provider may package its resource bundles in the
same package as the base name of the resource bundle if the package
is not split among other named modules. If there are more than one
bundle providers providing the resource bundle of a given base name,
the resource bundles can be packaged with per-language grouping
or per-region grouping to eliminate the split packages.

For example, if

baseName

is

"p.resources.Bundle"

then
the resource bundle name of

"p.resources.Bundle"

of

Locale("ja", "", "XX")

and

Locale("en")

could be

"p.resources.ja.Bundle_ja_ _XX"

and

"p.resources.Bundle_en"

respectively.

This method is called from the default implementation of the

getBundle(String, Locale)

method.
**Implementation Note:** The default implementation of this method is the same as the
implementation of

ResourceBundle.Control.toBundleName(String, Locale)

.
**Parameters:** baseName

- the base name of the resource bundle, a fully qualified
class name
**Parameters:** locale

- the locale for which a resource bundle should be loaded
**Returns:** the bundle name for the resource bundle

- getBundle

```java
public
ResourceBundle
getBundle​(
String
baseName,

Locale
locale)
```

Returns a

ResourceBundle

for the given

baseName

and

locale

.

**Specified by:** getBundle

in interface

ResourceBundleProvider
**Implementation Note:** The default implementation of this method calls the

toBundleName

method to get the
bundle name for the

baseName

and

locale

and finds the
resource bundle of the bundle name local in the module of this provider.
It will only search the formats specified when this provider was
constructed.
**Parameters:** baseName

- the base bundle name of the resource bundle, a fully
qualified class name.
**Parameters:** locale

- the locale for which the resource bundle should be instantiated
**Returns:** ResourceBundle

of the given

baseName

and

locale

, or

null

if no resource bundle is found
**Throws:** NullPointerException

- if

baseName

or

locale

is

null
**Throws:** UncheckedIOException

- if any IO exception occurred during resource
bundle loading

---

#### Method Detail

toBundleName

```java
protected
String
toBundleName​(
String
baseName,

Locale
locale)
```

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

**API Note:** A resource bundle provider may package its resource bundles in the
same package as the base name of the resource bundle if the package
is not split among other named modules. If there are more than one
bundle providers providing the resource bundle of a given base name,
the resource bundles can be packaged with per-language grouping
or per-region grouping to eliminate the split packages.

For example, if

baseName

is

"p.resources.Bundle"

then
the resource bundle name of

"p.resources.Bundle"

of

Locale("ja", "", "XX")

and

Locale("en")

could be

"p.resources.ja.Bundle_ja_ _XX"

and

"p.resources.Bundle_en"

respectively.

This method is called from the default implementation of the

getBundle(String, Locale)

method.
**Implementation Note:** The default implementation of this method is the same as the
implementation of

ResourceBundle.Control.toBundleName(String, Locale)

.
**Parameters:** baseName

- the base name of the resource bundle, a fully qualified
class name
**Parameters:** locale

- the locale for which a resource bundle should be loaded
**Returns:** the bundle name for the resource bundle

---

#### toBundleName

protected

String

toBundleName​(

String

baseName,

Locale

locale)

Returns the bundle name for the given

baseName

and

locale

that this provider provides.

For example, if

baseName

is

"p.resources.Bundle"

then
the resource bundle name of

"p.resources.Bundle"

of

Locale("ja", "", "XX")

and

Locale("en")

could be

"p.resources.ja.Bundle_ja_ _XX"

and

"p.resources.Bundle_en"

respectively.

This method is called from the default implementation of the

getBundle(String, Locale)

method.

This method is called from the default implementation of the

getBundle(String, Locale)

method.

getBundle

```java
public
ResourceBundle
getBundle​(
String
baseName,

Locale
locale)
```

Returns a

ResourceBundle

for the given

baseName

and

locale

.

**Specified by:** getBundle

in interface

ResourceBundleProvider
**Implementation Note:** The default implementation of this method calls the

toBundleName

method to get the
bundle name for the

baseName

and

locale

and finds the
resource bundle of the bundle name local in the module of this provider.
It will only search the formats specified when this provider was
constructed.
**Parameters:** baseName

- the base bundle name of the resource bundle, a fully
qualified class name.
**Parameters:** locale

- the locale for which the resource bundle should be instantiated
**Returns:** ResourceBundle

of the given

baseName

and

locale

, or

null

if no resource bundle is found
**Throws:** NullPointerException

- if

baseName

or

locale

is

null
**Throws:** UncheckedIOException

- if any IO exception occurred during resource
bundle loading

---

#### getBundle

public

ResourceBundle

getBundle​(

String

baseName,

Locale

locale)

Returns a

ResourceBundle

for the given

baseName

and

locale

.

---

