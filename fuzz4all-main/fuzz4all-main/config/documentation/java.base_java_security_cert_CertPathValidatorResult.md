# Interface CertPathValidatorResult

**Source:** `java.base\java\security\cert\CertPathValidatorResult.html`

### Class Description

```java
public interface
CertPathValidatorResult

extends
Cloneable
```

A specification of the result of a certification path validator algorithm.

The purpose of this interface is to group (and provide type safety
for) all certification path validator results. All results returned
by the

CertPathValidator.validate

method must implement this interface.

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

CertPathValidatorResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:**
- a copy of this

CertPathValidatorResult

---

### Additional Sections

#### Interface CertPathValidatorResult

**All Superinterfaces:** Cloneable

**All Known Implementing Classes:** PKIXCertPathBuilderResult

,

PKIXCertPathValidatorResult

```java
public interface
CertPathValidatorResult

extends
Cloneable
```

A specification of the result of a certification path validator algorithm.

The purpose of this interface is to group (and provide type safety
for) all certification path validator results. All results returned
by the

CertPathValidator.validate

method must implement this interface.

**Since:** 1.4
**See Also:** CertPathValidator

public interface

CertPathValidatorResult

extends

Cloneable

A specification of the result of a certification path validator algorithm.

The purpose of this interface is to group (and provide type safety
for) all certification path validator results. All results returned
by the

CertPathValidator.validate

method must implement this interface.

The purpose of this interface is to group (and provide type safety
for) all certification path validator results. All results returned
by the

CertPathValidator.validate

method must implement this interface.

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

CertPathValidatorResult

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

CertPathValidatorResult

.

---

#### Method Summary

Makes a copy of this

CertPathValidatorResult

.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathValidatorResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathValidatorResult

Method Detail

- clone

```java
Object
clone()
```

Makes a copy of this

CertPathValidatorResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathValidatorResult

---

#### Method Detail

clone

```java
Object
clone()
```

Makes a copy of this

CertPathValidatorResult

. Changes to the
copy will not affect the original and vice versa.

**Returns:** a copy of this

CertPathValidatorResult

---

#### clone

Object

clone()

Makes a copy of this

CertPathValidatorResult

. Changes to the
copy will not affect the original and vice versa.

---

