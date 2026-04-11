# Interface ModuleElement.RequiresDirective

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.RequiresDirective.html`

### Class Description

```java
public static interface
ModuleElement.RequiresDirective

extends
ModuleElement.Directive
```

A dependency of a module.

**All Superinterfaces:** ModuleElement.Directive

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isStatic()

Returns whether or not this is a static dependency.

**Returns:**
- whether or not this is a static dependency

---

#### boolean isTransitive()

Returns whether or not this is a transitive dependency.

**Returns:**
- whether or not this is a transitive dependency

---

#### ModuleElement
getDependency()

Returns the module that is required

**Returns:**
- the module that is required

---

### Additional Sections

#### Interface ModuleElement.RequiresDirective

**All Superinterfaces:** ModuleElement.Directive

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.RequiresDirective

extends
ModuleElement.Directive
```

A dependency of a module.

**Since:** 9

public static interface

ModuleElement.RequiresDirective

extends

ModuleElement.Directive

A dependency of a module.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ModuleElement

getDependency

()

Returns the module that is required

boolean

isStatic

()

Returns whether or not this is a static dependency.

boolean

isTransitive

()

Returns whether or not this is a transitive dependency.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ModuleElement

getDependency

()

Returns the module that is required

boolean

isStatic

()

Returns whether or not this is a static dependency.

boolean

isTransitive

()

Returns whether or not this is a transitive dependency.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Method Summary

Returns the module that is required

Returns whether or not this is a static dependency.

Returns whether or not this is a transitive dependency.

Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Methods declared in interface javax.lang.model.element. ModuleElement.Directive

============ METHOD DETAIL ==========

- Method Detail

- isStatic

```java
boolean isStatic()
```

Returns whether or not this is a static dependency.

**Returns:** whether or not this is a static dependency

- isTransitive

```java
boolean isTransitive()
```

Returns whether or not this is a transitive dependency.

**Returns:** whether or not this is a transitive dependency

- getDependency

```java
ModuleElement
getDependency()
```

Returns the module that is required

**Returns:** the module that is required

Method Detail

- isStatic

```java
boolean isStatic()
```

Returns whether or not this is a static dependency.

**Returns:** whether or not this is a static dependency

- isTransitive

```java
boolean isTransitive()
```

Returns whether or not this is a transitive dependency.

**Returns:** whether or not this is a transitive dependency

- getDependency

```java
ModuleElement
getDependency()
```

Returns the module that is required

**Returns:** the module that is required

---

#### Method Detail

isStatic

```java
boolean isStatic()
```

Returns whether or not this is a static dependency.

**Returns:** whether or not this is a static dependency

---

#### isStatic

boolean isStatic()

Returns whether or not this is a static dependency.

isTransitive

```java
boolean isTransitive()
```

Returns whether or not this is a transitive dependency.

**Returns:** whether or not this is a transitive dependency

---

#### isTransitive

boolean isTransitive()

Returns whether or not this is a transitive dependency.

getDependency

```java
ModuleElement
getDependency()
```

Returns the module that is required

**Returns:** the module that is required

---

#### getDependency

ModuleElement

getDependency()

Returns the module that is required

---

