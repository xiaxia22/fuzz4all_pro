# Interface ModuleElement.ExportsDirective

**Source:** `java.compiler\javax\lang\model\element\ModuleElement.ExportsDirective.html`

### Class Description

```java
public static interface
ModuleElement.ExportsDirective

extends
ModuleElement.Directive
```

An exported package of a module.

**All Superinterfaces:** ModuleElement.Directive

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### PackageElement
getPackage()

Returns the package being exported.

**Returns:**
- the package being exported

---

#### List
<? extends
ModuleElement
> getTargetModules()

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

**Returns:**
- the specific modules to which the package is being exported

---

### Additional Sections

#### Interface ModuleElement.ExportsDirective

**All Superinterfaces:** ModuleElement.Directive

**Enclosing interface:** ModuleElement

```java
public static interface
ModuleElement.ExportsDirective

extends
ModuleElement.Directive
```

An exported package of a module.

**Since:** 9

public static interface

ModuleElement.ExportsDirective

extends

ModuleElement.Directive

An exported package of a module.

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

Returns the package being exported.

List

<? extends

ModuleElement

>

getTargetModules

()

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
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

Returns the package being exported.

List

<? extends

ModuleElement

>

getTargetModules

()

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

- Methods declared in interface javax.lang.model.element.

ModuleElement.Directive

accept

,

getKind

---

#### Method Summary

Returns the package being exported.

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
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

Returns the package being exported.

**Returns:** the package being exported

- getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being exported

Method Detail

- getPackage

```java
PackageElement
getPackage()
```

Returns the package being exported.

**Returns:** the package being exported

- getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being exported

---

#### Method Detail

getPackage

```java
PackageElement
getPackage()
```

Returns the package being exported.

**Returns:** the package being exported

---

#### getPackage

PackageElement

getPackage()

Returns the package being exported.

getTargetModules

```java
List
<? extends
ModuleElement
> getTargetModules()
```

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

**Returns:** the specific modules to which the package is being exported

---

#### getTargetModules

List

<? extends

ModuleElement

> getTargetModules()

Returns the specific modules to which the package is being exported,
or null, if the package is exported to all modules which
have readability to this module.

---

