# Interface ModuleElement.OpensDirective

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.OpensDirective.html`

### Class Description

```java
public static interface
ModuleElement.OpensDirective

extends
ModuleElement.Directive
```

An opened package of a module.

**All Superinterfaces:** ModuleElement.Directive

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### PackageElement
getPackage()

Returns the package being opened.

**Returns:**
- the package being opened

---

#### List
<? extends
ModuleElement
> getTargetModules()

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

**Returns:**
- the specific modules to which the package is being opened

---

### Additional Sections

#### Interface ModuleElement.OpensDirective

**All Superinterfaces:** ModuleElement.Directive

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.OpensDirective

extends
ModuleElement.Directive
```

An opened package of a module.

**Since:** 9

public static interface

ModuleElement.OpensDirective

extends

ModuleElement.Directive

An opened package of a module.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

PackageElement

getPackage

()

Returns the package being opened.

List

<? extends

ModuleElement

>

getTargetModules

()

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

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

PackageElement

getPackage

()

Returns the package being opened.

List

<? extends

ModuleElement

>

getTargetModules

()

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Method Summary

Returns the package being opened.

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Methods declared in interface javax.lang.model.element. ModuleElement.Directive

============ METHOD DETAIL ==========

- Method Detail

- getPackage

```java
PackageElement
getPackage()
```

Returns the package being opened.

**Returns:** the package being opened

- getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being opened

Method Detail

- getPackage

```java
PackageElement
getPackage()
```

Returns the package being opened.

**Returns:** the package being opened

- getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being opened

---

#### Method Detail

getPackage

```java
PackageElement
getPackage()
```

Returns the package being opened.

**Returns:** the package being opened

---

#### getPackage

PackageElement

getPackage()

Returns the package being opened.

getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being opened

---

#### getTargetModules

List

<? extends

ModuleElement

> getTargetModules()

Returns the specific modules to which the package is being open
or null, if the package is open all modules which
have readability to this module.

---

