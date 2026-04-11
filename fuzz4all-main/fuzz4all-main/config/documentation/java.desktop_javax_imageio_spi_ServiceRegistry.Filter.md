# Interface ServiceRegistry.Filter

**Source:** `java.desktop\javax\imageio\spi\ServiceRegistry.Filter.html`

### Class Description

```java
public static interface
ServiceRegistry.Filter
```

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion. Classes that
implement this interface should be defined in order to make use
of the

getServiceProviders

method of

ServiceRegistry

that takes a

Filter

.

**Enclosing class:** ServiceRegistry

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean filter​(
Object
provider)

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

**Parameters:**
- provider

- a service provider

Object

.

**Returns:**
- true if the provider matches the criterion.

---

### Additional Sections

#### Interface ServiceRegistry.Filter

**Enclosing class:** ServiceRegistry

```java
public static interface
ServiceRegistry.Filter
```

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion. Classes that
implement this interface should be defined in order to make use
of the

getServiceProviders

method of

ServiceRegistry

that takes a

Filter

.

**See Also:** ServiceRegistry.getServiceProviders(Class, ServiceRegistry.Filter, boolean)

public static interface

ServiceRegistry.Filter

A simple filter interface used by

ServiceRegistry.getServiceProviders

to select
providers matching an arbitrary criterion. Classes that
implement this interface should be defined in order to make use
of the

getServiceProviders

method of

ServiceRegistry

that takes a

Filter

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

filter

​(

Object

provider)

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

filter

​(

Object

provider)

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

---

#### Method Summary

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

============ METHOD DETAIL ==========

- Method Detail

- filter

```java
boolean filter​(
Object
provider)
```

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

**Parameters:** provider

- a service provider

Object

.
**Returns:** true if the provider matches the criterion.

Method Detail

- filter

```java
boolean filter​(
Object
provider)
```

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

**Parameters:** provider

- a service provider

Object

.
**Returns:** true if the provider matches the criterion.

---

#### Method Detail

filter

```java
boolean filter​(
Object
provider)
```

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

**Parameters:** provider

- a service provider

Object

.
**Returns:** true if the provider matches the criterion.

---

#### filter

boolean filter​(

Object

provider)

Returns

true

if the given

provider

object matches the criterion defined
by this

Filter

.

---

