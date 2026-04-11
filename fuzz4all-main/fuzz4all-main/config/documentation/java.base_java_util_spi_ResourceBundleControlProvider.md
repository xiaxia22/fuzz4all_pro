# Interface ResourceBundleControlProvider

**Source:** `java.base\java\util\spi\ResourceBundleControlProvider.html`

### Class Description

```java
public interface
ResourceBundleControlProvider
```

An interface for service providers that provide implementations of

ResourceBundle.Control

. The

default resource bundle loading
behavior

of the

ResourceBundle.getBundle

factory methods that take
no

ResourceBundle.Control

instance can be modified with

ResourceBundleControlProvider

implementations.

Provider implementations are loaded from the application's class path
using

ServiceLoader

at the first invocation of the

ResourceBundle.getBundle

factory method that takes no

ResourceBundle.Control

instance.

All

ResourceBundleControlProvider

s are ignored in named modules.

**Since:** 1.8
**See Also:** ResourceBundle.getBundle

,

ServiceLoader.load(Class)

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ResourceBundle.Control
getControl​(
String
baseName)

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

. This method must return

null

if the given

baseName

isn't handled by this provider.

**Parameters:**
- baseName

- the base name of the resource bundle

**Returns:**
- a

ResourceBundle.Control

instance,
or

null

if the given

baseName

is not
applicable to this provider.

**Throws:**
- NullPointerException

- if

baseName

is

null

---

### Additional Sections

#### Interface ResourceBundleControlProvider

```java
public interface
ResourceBundleControlProvider
```

An interface for service providers that provide implementations of

ResourceBundle.Control

. The

default resource bundle loading
behavior

of the

ResourceBundle.getBundle

factory methods that take
no

ResourceBundle.Control

instance can be modified with

ResourceBundleControlProvider

implementations.

Provider implementations are loaded from the application's class path
using

ServiceLoader

at the first invocation of the

ResourceBundle.getBundle

factory method that takes no

ResourceBundle.Control

instance.

All

ResourceBundleControlProvider

s are ignored in named modules.

**Since:** 1.8
**See Also:** ResourceBundle.getBundle

,

ServiceLoader.load(Class)

public interface

ResourceBundleControlProvider

An interface for service providers that provide implementations of

ResourceBundle.Control

. The

default resource bundle loading
behavior

of the

ResourceBundle.getBundle

factory methods that take
no

ResourceBundle.Control

instance can be modified with

ResourceBundleControlProvider

implementations.

Provider implementations are loaded from the application's class path
using

ServiceLoader

at the first invocation of the

ResourceBundle.getBundle

factory method that takes no

ResourceBundle.Control

instance.

All

ResourceBundleControlProvider

s are ignored in named modules.

Provider implementations are loaded from the application's class path
using

ServiceLoader

at the first invocation of the

ResourceBundle.getBundle

factory method that takes no

ResourceBundle.Control

instance.

All

ResourceBundleControlProvider

s are ignored in named modules.

All

ResourceBundleControlProvider

s are ignored in named modules.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ResourceBundle.Control

getControl

​(

String

baseName)

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ResourceBundle.Control

getControl

​(

String

baseName)

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

.

---

#### Method Summary

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

.

============ METHOD DETAIL ==========

- Method Detail

- getControl

```java
ResourceBundle.Control
getControl​(
String
baseName)
```

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

. This method must return

null

if the given

baseName

isn't handled by this provider.

**Parameters:** baseName

- the base name of the resource bundle
**Returns:** a

ResourceBundle.Control

instance,
or

null

if the given

baseName

is not
applicable to this provider.
**Throws:** NullPointerException

- if

baseName

is

null

Method Detail

- getControl

```java
ResourceBundle.Control
getControl​(
String
baseName)
```

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

. This method must return

null

if the given

baseName

isn't handled by this provider.

**Parameters:** baseName

- the base name of the resource bundle
**Returns:** a

ResourceBundle.Control

instance,
or

null

if the given

baseName

is not
applicable to this provider.
**Throws:** NullPointerException

- if

baseName

is

null

---

#### Method Detail

getControl

```java
ResourceBundle.Control
getControl​(
String
baseName)
```

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

. This method must return

null

if the given

baseName

isn't handled by this provider.

**Parameters:** baseName

- the base name of the resource bundle
**Returns:** a

ResourceBundle.Control

instance,
or

null

if the given

baseName

is not
applicable to this provider.
**Throws:** NullPointerException

- if

baseName

is

null

---

#### getControl

ResourceBundle.Control

getControl​(

String

baseName)

Returns a

ResourceBundle.Control

instance that is used
to handle resource bundle loading for the given

baseName

. This method must return

null

if the given

baseName

isn't handled by this provider.

---

