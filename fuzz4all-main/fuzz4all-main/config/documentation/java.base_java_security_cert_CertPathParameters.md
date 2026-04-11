# Interface CertPathParameters

**Source:** `java.base\java\security\cert\CertPathParameters.html`

### Class Description

```java
public interface
CertPathParameters

extends
Cloneable
```

A specification of certification path algorithm parameters.
The purpose of this interface is to group (and provide type safety for)
all

CertPath

parameter specifications. All

CertPath

parameter specifications must implement this
interface.

**All Superinterfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
clone()

Makes a copy of this

CertPathParameters

. Changes to the
copy will not affect the original and vice versa.

**Returns:**
- a copy of this

CertPathParameters

---

### Additional Sections

#### Interface CertPathParameters

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** PKIXBuilderParameters

,

PKIXParameters

```java
public interface
CertPathParameters

extends
Cloneable
```

A specification of certification path algorithm parameters.
The purpose of this interface is to group (and provide type safety for)
all

CertPath

parameter specifications. All

CertPath

parameter specifications must implement this
interface.

**Since:** 1.4
**See Also:** CertPathValidator.validate(CertPath, CertPathParameters)

,

CertPathBuilder.build(CertPathParameters)

public interface

CertPathParameters

extends

Cloneable

A specification of certification path algorithm parameters.
The purpose of this interface is to group (and provide type safety for)
all

CertPath

parameter specifications. All

CertPath

parameter specifications must implement this
interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CertPathParameters

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

clone

()

Makes a copy of this

CertPathParameters

.

---

#### Method Summary

Makes a copy of this

CertPathParameters

.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathParameters

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathParameters

Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathParameters

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathParameters

---

#### Method Detail

clone

```java
Object
clone()
```

Makes a copy of this

CertPathParameters

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathParameters

---

#### clone

Object

clone()

Makes a copy of this

CertPathParameters

. Changes to the
copy will not affect the original and vice versa.

---

