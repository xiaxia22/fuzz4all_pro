# Class GraphicsConfigTemplate

**Source:** `java.desktop\java\awt\GraphicsConfigTemplate.html`

### Class Description

```java
public abstract class
GraphicsConfigTemplate

extends
Object

implements
Serializable
```

The

GraphicsConfigTemplate

class is used to obtain a valid

GraphicsConfiguration

. A user instantiates one of these
objects and then sets all non-default attributes as desired. The

GraphicsDevice.getBestConfiguration(java.awt.GraphicsConfigTemplate)

method found in the

GraphicsDevice

class is then called with this

GraphicsConfigTemplate

. A valid

GraphicsConfiguration

is returned that meets or exceeds
what was requested in the

GraphicsConfigTemplate

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int REQUIRED

Value used for "Enum" (Integer) type. States that this
feature is required for the

GraphicsConfiguration

object. If this feature is not available, do not select the

GraphicsConfiguration

object.

**See Also:**
- Constant Field Values

---

#### public static final int PREFERRED

Value used for "Enum" (Integer) type. States that this
feature is desired for the

GraphicsConfiguration

object. A selection with this feature is preferred over a
selection that does not include this feature, although both
selections can be considered valid matches.

**See Also:**
- Constant Field Values

---

#### public static final int UNNECESSARY

Value used for "Enum" (Integer) type. States that this
feature is not necessary for the selection of the

GraphicsConfiguration

object. A selection
without this feature is preferred over a selection that
includes this feature since it is not used.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public GraphicsConfigTemplate()

This class is an abstract class so only subclasses can be
instantiated.

---

### Method Details

#### public abstract
GraphicsConfiguration
getBestConfiguration​(
GraphicsConfiguration
[] gc)

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

**Parameters:**
- gc

- the array of

GraphicsConfiguration

objects to choose from.

**Returns:**
- a

GraphicsConfiguration

object that is
the best configuration possible.

**See Also:**
- GraphicsConfiguration

---

#### public abstract boolean isGraphicsConfigSupported​(
GraphicsConfiguration
gc)

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

**Parameters:**
- gc

- the

GraphicsConfiguration

object to test

**Returns:**
- true

if this

GraphicsConfiguration

object can be used to create
surfaces that support the indicated features;

false

if the

GraphicsConfiguration

can
not be used to create a drawing surface usable by this Java(tm)
API.

---

### Additional Sections

#### Class GraphicsConfigTemplate

java.lang.Object

- java.awt.GraphicsConfigTemplate

java.awt.GraphicsConfigTemplate

**All Implemented Interfaces:** Serializable

```java
public abstract class
GraphicsConfigTemplate

extends
Object

implements
Serializable
```

The

GraphicsConfigTemplate

class is used to obtain a valid

GraphicsConfiguration

. A user instantiates one of these
objects and then sets all non-default attributes as desired. The

GraphicsDevice.getBestConfiguration(java.awt.GraphicsConfigTemplate)

method found in the

GraphicsDevice

class is then called with this

GraphicsConfigTemplate

. A valid

GraphicsConfiguration

is returned that meets or exceeds
what was requested in the

GraphicsConfigTemplate

.

**Since:** 1.2
**See Also:** GraphicsDevice

,

GraphicsConfiguration

,

Serialized Form

public abstract class

GraphicsConfigTemplate

extends

Object

implements

Serializable

The

GraphicsConfigTemplate

class is used to obtain a valid

GraphicsConfiguration

. A user instantiates one of these
objects and then sets all non-default attributes as desired. The

GraphicsDevice.getBestConfiguration(java.awt.GraphicsConfigTemplate)

method found in the

GraphicsDevice

class is then called with this

GraphicsConfigTemplate

. A valid

GraphicsConfiguration

is returned that meets or exceeds
what was requested in the

GraphicsConfigTemplate

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

PREFERRED

Value used for "Enum" (Integer) type.

static int

REQUIRED

Value used for "Enum" (Integer) type.

static int

UNNECESSARY

Value used for "Enum" (Integer) type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GraphicsConfigTemplate

()

This class is an abstract class so only subclasses can be
instantiated.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

GraphicsConfiguration

getBestConfiguration

​(

GraphicsConfiguration

[] gc)

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

abstract boolean

isGraphicsConfigSupported

​(

GraphicsConfiguration

gc)

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

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

static int

PREFERRED

Value used for "Enum" (Integer) type.

static int

REQUIRED

Value used for "Enum" (Integer) type.

static int

UNNECESSARY

Value used for "Enum" (Integer) type.

---

#### Field Summary

Value used for "Enum" (Integer) type.

Constructor Summary

Constructors

Constructor

Description

GraphicsConfigTemplate

()

This class is an abstract class so only subclasses can be
instantiated.

---

#### Constructor Summary

This class is an abstract class so only subclasses can be
instantiated.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

GraphicsConfiguration

getBestConfiguration

​(

GraphicsConfiguration

[] gc)

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

abstract boolean

isGraphicsConfigSupported

​(

GraphicsConfiguration

gc)

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

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

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

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

- REQUIRED

```java
public static final int REQUIRED
```

Value used for "Enum" (Integer) type. States that this
feature is required for the

GraphicsConfiguration

object. If this feature is not available, do not select the

GraphicsConfiguration

object.

**See Also:** Constant Field Values

- PREFERRED

```java
public static final int PREFERRED
```

Value used for "Enum" (Integer) type. States that this
feature is desired for the

GraphicsConfiguration

object. A selection with this feature is preferred over a
selection that does not include this feature, although both
selections can be considered valid matches.

**See Also:** Constant Field Values

- UNNECESSARY

```java
public static final int UNNECESSARY
```

Value used for "Enum" (Integer) type. States that this
feature is not necessary for the selection of the

GraphicsConfiguration

object. A selection
without this feature is preferred over a selection that
includes this feature since it is not used.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GraphicsConfigTemplate

```java
public GraphicsConfigTemplate()
```

This class is an abstract class so only subclasses can be
instantiated.

============ METHOD DETAIL ==========

- Method Detail

- getBestConfiguration

```java
public abstract
GraphicsConfiguration
getBestConfiguration​(
GraphicsConfiguration
[] gc)
```

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

**Parameters:** gc

- the array of

GraphicsConfiguration

objects to choose from.
**Returns:** a

GraphicsConfiguration

object that is
the best configuration possible.
**See Also:** GraphicsConfiguration

- isGraphicsConfigSupported

```java
public abstract boolean isGraphicsConfigSupported​(
GraphicsConfiguration
gc)
```

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

**Parameters:** gc

- the

GraphicsConfiguration

object to test
**Returns:** true

if this

GraphicsConfiguration

object can be used to create
surfaces that support the indicated features;

false

if the

GraphicsConfiguration

can
not be used to create a drawing surface usable by this Java(tm)
API.

Field Detail

- REQUIRED

```java
public static final int REQUIRED
```

Value used for "Enum" (Integer) type. States that this
feature is required for the

GraphicsConfiguration

object. If this feature is not available, do not select the

GraphicsConfiguration

object.

**See Also:** Constant Field Values

- PREFERRED

```java
public static final int PREFERRED
```

Value used for "Enum" (Integer) type. States that this
feature is desired for the

GraphicsConfiguration

object. A selection with this feature is preferred over a
selection that does not include this feature, although both
selections can be considered valid matches.

**See Also:** Constant Field Values

- UNNECESSARY

```java
public static final int UNNECESSARY
```

Value used for "Enum" (Integer) type. States that this
feature is not necessary for the selection of the

GraphicsConfiguration

object. A selection
without this feature is preferred over a selection that
includes this feature since it is not used.

**See Also:** Constant Field Values

---

#### Field Detail

REQUIRED

```java
public static final int REQUIRED
```

Value used for "Enum" (Integer) type. States that this
feature is required for the

GraphicsConfiguration

object. If this feature is not available, do not select the

GraphicsConfiguration

object.

**See Also:** Constant Field Values

---

#### REQUIRED

public static final int REQUIRED

Value used for "Enum" (Integer) type. States that this
feature is required for the

GraphicsConfiguration

object. If this feature is not available, do not select the

GraphicsConfiguration

object.

PREFERRED

```java
public static final int PREFERRED
```

Value used for "Enum" (Integer) type. States that this
feature is desired for the

GraphicsConfiguration

object. A selection with this feature is preferred over a
selection that does not include this feature, although both
selections can be considered valid matches.

**See Also:** Constant Field Values

---

#### PREFERRED

public static final int PREFERRED

Value used for "Enum" (Integer) type. States that this
feature is desired for the

GraphicsConfiguration

object. A selection with this feature is preferred over a
selection that does not include this feature, although both
selections can be considered valid matches.

UNNECESSARY

```java
public static final int UNNECESSARY
```

Value used for "Enum" (Integer) type. States that this
feature is not necessary for the selection of the

GraphicsConfiguration

object. A selection
without this feature is preferred over a selection that
includes this feature since it is not used.

**See Also:** Constant Field Values

---

#### UNNECESSARY

public static final int UNNECESSARY

Value used for "Enum" (Integer) type. States that this
feature is not necessary for the selection of the

GraphicsConfiguration

object. A selection
without this feature is preferred over a selection that
includes this feature since it is not used.

Constructor Detail

- GraphicsConfigTemplate

```java
public GraphicsConfigTemplate()
```

This class is an abstract class so only subclasses can be
instantiated.

---

#### Constructor Detail

GraphicsConfigTemplate

```java
public GraphicsConfigTemplate()
```

This class is an abstract class so only subclasses can be
instantiated.

---

#### GraphicsConfigTemplate

public GraphicsConfigTemplate()

This class is an abstract class so only subclasses can be
instantiated.

Method Detail

- getBestConfiguration

```java
public abstract
GraphicsConfiguration
getBestConfiguration​(
GraphicsConfiguration
[] gc)
```

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

**Parameters:** gc

- the array of

GraphicsConfiguration

objects to choose from.
**Returns:** a

GraphicsConfiguration

object that is
the best configuration possible.
**See Also:** GraphicsConfiguration

- isGraphicsConfigSupported

```java
public abstract boolean isGraphicsConfigSupported​(
GraphicsConfiguration
gc)
```

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

**Parameters:** gc

- the

GraphicsConfiguration

object to test
**Returns:** true

if this

GraphicsConfiguration

object can be used to create
surfaces that support the indicated features;

false

if the

GraphicsConfiguration

can
not be used to create a drawing surface usable by this Java(tm)
API.

---

#### Method Detail

getBestConfiguration

```java
public abstract
GraphicsConfiguration
getBestConfiguration​(
GraphicsConfiguration
[] gc)
```

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

**Parameters:** gc

- the array of

GraphicsConfiguration

objects to choose from.
**Returns:** a

GraphicsConfiguration

object that is
the best configuration possible.
**See Also:** GraphicsConfiguration

---

#### getBestConfiguration

public abstract

GraphicsConfiguration

getBestConfiguration​(

GraphicsConfiguration

[] gc)

Returns the "best" configuration possible that passes the
criteria defined in the

GraphicsConfigTemplate

.

isGraphicsConfigSupported

```java
public abstract boolean isGraphicsConfigSupported​(
GraphicsConfiguration
gc)
```

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

**Parameters:** gc

- the

GraphicsConfiguration

object to test
**Returns:** true

if this

GraphicsConfiguration

object can be used to create
surfaces that support the indicated features;

false

if the

GraphicsConfiguration

can
not be used to create a drawing surface usable by this Java(tm)
API.

---

#### isGraphicsConfigSupported

public abstract boolean isGraphicsConfigSupported​(

GraphicsConfiguration

gc)

Returns a

boolean

indicating whether or
not the specified

GraphicsConfiguration

can be
used to create a drawing surface that supports the indicated
features.

---

