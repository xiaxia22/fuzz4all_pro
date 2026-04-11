# Class ModuleLayer.Controller

**Source:** `java.base\java\lang\ModuleLayer.Controller.html`

### Class Description

```java
public static final class
ModuleLayer.Controller

extends
Object
```

Controls a module layer. The static methods defined by

ModuleLayer

to create module layers return a

Controller

that can be used to
control modules in the layer.

Unless otherwise specified, passing a

null

argument to a
method in this class causes a

NullPointerException

to be thrown.

**Enclosing class:** ModuleLayer

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
ModuleLayer
layer()

Returns the layer that this object controls.

**Returns:**
- the module layer

---

#### public
ModuleLayer.Controller
addReads​(
Module
source,

Module
target)

Updates module

source

in the layer to read module

target

. This method is a no-op if

source

already
reads

target

.

**Parameters:**
- source

- The source module
- target

- The target module to read

**Returns:**
- This controller

**Throws:**
- IllegalArgumentException

- If

source

is not in the module layer

**See Also:**
- Module.addReads(java.lang.Module)

**Implementation Note:**
- Read edges

added by this method are

weak

and do not prevent

target

from being GC'ed when

source

is strongly reachable.

---

#### public
ModuleLayer.Controller
addExports​(
Module
source,

String
pn,

Module
target)

Updates module

source

in the layer to export a package to
module

target

. This method is a no-op if

source

already exports the package to at least

target

.

**Parameters:**
- source

- The source module
- pn

- The package name
- target

- The target module

**Returns:**
- This controller

**Throws:**
- IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module

**See Also:**
- Module.addExports(java.lang.String, java.lang.Module)

---

#### public
ModuleLayer.Controller
addOpens​(
Module
source,

String
pn,

Module
target)

Updates module

source

in the layer to open a package to
module

target

. This method is a no-op if

source

already opens the package to at least

target

.

**Parameters:**
- source

- The source module
- pn

- The package name
- target

- The target module

**Returns:**
- This controller

**Throws:**
- IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module

**See Also:**
- Module.addOpens(java.lang.String, java.lang.Module)

---

### Additional Sections

#### Class ModuleLayer.Controller

java.lang.Object

- java.lang.ModuleLayer.Controller

java.lang.ModuleLayer.Controller

**Enclosing class:** ModuleLayer

```java
public static final class
ModuleLayer.Controller

extends
Object
```

Controls a module layer. The static methods defined by

ModuleLayer

to create module layers return a

Controller

that can be used to
control modules in the layer.

Unless otherwise specified, passing a

null

argument to a
method in this class causes a

NullPointerException

to be thrown.

**API Note:** Care should be taken with

Controller

objects, they
should never be shared with untrusted code.
**Since:** 9

public static final class

ModuleLayer.Controller

extends

Object

Controls a module layer. The static methods defined by

ModuleLayer

to create module layers return a

Controller

that can be used to
control modules in the layer.

Unless otherwise specified, passing a

null

argument to a
method in this class causes a

NullPointerException

to be thrown.

Unless otherwise specified, passing a

null

argument to a
method in this class causes a

NullPointerException

to be thrown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ModuleLayer.Controller

addExports

​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to export a package to
module

target

.

ModuleLayer.Controller

addOpens

​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to open a package to
module

target

.

ModuleLayer.Controller

addReads

​(

Module

source,

Module

target)

Updates module

source

in the layer to read module

target

.

ModuleLayer

layer

()

Returns the layer that this object controls.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ModuleLayer.Controller

addExports

​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to export a package to
module

target

.

ModuleLayer.Controller

addOpens

​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to open a package to
module

target

.

ModuleLayer.Controller

addReads

​(

Module

source,

Module

target)

Updates module

source

in the layer to read module

target

.

ModuleLayer

layer

()

Returns the layer that this object controls.

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

Updates module

source

in the layer to export a package to
module

target

.

Updates module

source

in the layer to open a package to
module

target

.

Updates module

source

in the layer to read module

target

.

Returns the layer that this object controls.

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

============ METHOD DETAIL ==========

- Method Detail

- layer

```java
public
ModuleLayer
layer()
```

Returns the layer that this object controls.

**Returns:** the module layer

- addReads

```java
public
ModuleLayer.Controller
addReads​(
Module
source,

Module
target)
```

Updates module

source

in the layer to read module

target

. This method is a no-op if

source

already
reads

target

.

**Implementation Note:** Read edges

added by this method are

weak

and do not prevent

target

from being GC'ed when

source

is strongly reachable.
**Parameters:** source

- The source module
**Parameters:** target

- The target module to read
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer
**See Also:** Module.addReads(java.lang.Module)

- addExports

```java
public
ModuleLayer.Controller
addExports​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to export a package to
module

target

. This method is a no-op if

source

already exports the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addExports(java.lang.String, java.lang.Module)

- addOpens

```java
public
ModuleLayer.Controller
addOpens​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to open a package to
module

target

. This method is a no-op if

source

already opens the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addOpens(java.lang.String, java.lang.Module)

Method Detail

- layer

```java
public
ModuleLayer
layer()
```

Returns the layer that this object controls.

**Returns:** the module layer

- addReads

```java
public
ModuleLayer.Controller
addReads​(
Module
source,

Module
target)
```

Updates module

source

in the layer to read module

target

. This method is a no-op if

source

already
reads

target

.

**Implementation Note:** Read edges

added by this method are

weak

and do not prevent

target

from being GC'ed when

source

is strongly reachable.
**Parameters:** source

- The source module
**Parameters:** target

- The target module to read
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer
**See Also:** Module.addReads(java.lang.Module)

- addExports

```java
public
ModuleLayer.Controller
addExports​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to export a package to
module

target

. This method is a no-op if

source

already exports the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addExports(java.lang.String, java.lang.Module)

- addOpens

```java
public
ModuleLayer.Controller
addOpens​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to open a package to
module

target

. This method is a no-op if

source

already opens the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addOpens(java.lang.String, java.lang.Module)

---

#### Method Detail

layer

```java
public
ModuleLayer
layer()
```

Returns the layer that this object controls.

**Returns:** the module layer

---

#### layer

public

ModuleLayer

layer()

Returns the layer that this object controls.

addReads

```java
public
ModuleLayer.Controller
addReads​(
Module
source,

Module
target)
```

Updates module

source

in the layer to read module

target

. This method is a no-op if

source

already
reads

target

.

**Implementation Note:** Read edges

added by this method are

weak

and do not prevent

target

from being GC'ed when

source

is strongly reachable.
**Parameters:** source

- The source module
**Parameters:** target

- The target module to read
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer
**See Also:** Module.addReads(java.lang.Module)

---

#### addReads

public

ModuleLayer.Controller

addReads​(

Module

source,

Module

target)

Updates module

source

in the layer to read module

target

. This method is a no-op if

source

already
reads

target

.

addExports

```java
public
ModuleLayer.Controller
addExports​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to export a package to
module

target

. This method is a no-op if

source

already exports the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addExports(java.lang.String, java.lang.Module)

---

#### addExports

public

ModuleLayer.Controller

addExports​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to export a package to
module

target

. This method is a no-op if

source

already exports the package to at least

target

.

addOpens

```java
public
ModuleLayer.Controller
addOpens​(
Module
source,

String
pn,

Module
target)
```

Updates module

source

in the layer to open a package to
module

target

. This method is a no-op if

source

already opens the package to at least

target

.

**Parameters:** source

- The source module
**Parameters:** pn

- The package name
**Parameters:** target

- The target module
**Returns:** This controller
**Throws:** IllegalArgumentException

- If

source

is not in the module layer or the package
is not in the source module
**See Also:** Module.addOpens(java.lang.String, java.lang.Module)

---

#### addOpens

public

ModuleLayer.Controller

addOpens​(

Module

source,

String

pn,

Module

target)

Updates module

source

in the layer to open a package to
module

target

. This method is a no-op if

source

already opens the package to at least

target

.

---

