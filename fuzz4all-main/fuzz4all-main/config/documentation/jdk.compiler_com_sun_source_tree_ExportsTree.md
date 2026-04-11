# Interface ExportsTree

**Source:** `jdk.compiler\com\sun\source\tree\ExportsTree.html`

### Class Description

```java
public interface
ExportsTree

extends
DirectiveTree
```

A tree node for an 'exports' directive in a module declaration.

For example:

```java
exports
package-name
;
exports
package-name
to
module-name
;
```

**All Superinterfaces:** DirectiveTree

,

Tree

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ExpressionTree
getPackageName()

Returns the name of the package to be exported.

**Returns:**
- the name of the package to be exported

---

#### List
<? extends
ExpressionTree
> getModuleNames()

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

**Returns:**
- the names of the modules to which the package is exported, or null

---

### Additional Sections

#### Interface ExportsTree

**All Superinterfaces:** DirectiveTree

,

Tree

```java
public interface
ExportsTree

extends
DirectiveTree
```

A tree node for an 'exports' directive in a module declaration.

For example:

```java
exports
package-name
;
exports
package-name
to
module-name
;
```

**Since:** 9

public interface

ExportsTree

extends

DirectiveTree

A tree node for an 'exports' directive in a module declaration.

For example:

```java
exports
package-name
;
exports
package-name
to
module-name
;
```

exports

package-name

;
exports

package-name

to

module-name

;

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ExpressionTree

>

getModuleNames

()

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

ExpressionTree

getPackageName

()

Returns the name of the package to be exported.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

Nested Class Summary

- Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested Class Summary

Nested classes/interfaces declared in interface com.sun.source.tree.

Tree

Tree.Kind

---

#### Nested classes/interfaces declared in interface com.sun.source.tree. Tree

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

ExpressionTree

>

getModuleNames

()

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

ExpressionTree

getPackageName

()

Returns the name of the package to be exported.

- Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Method Summary

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

Returns the name of the package to be exported.

Methods declared in interface com.sun.source.tree.

Tree

accept

,

getKind

---

#### Methods declared in interface com.sun.source.tree. Tree

============ METHOD DETAIL ==========

- Method Detail

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be exported.

**Returns:** the name of the package to be exported

- getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

**Returns:** the names of the modules to which the package is exported, or null

Method Detail

- getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be exported.

**Returns:** the name of the package to be exported

- getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

**Returns:** the names of the modules to which the package is exported, or null

---

#### Method Detail

getPackageName

```java
ExpressionTree
getPackageName()
```

Returns the name of the package to be exported.

**Returns:** the name of the package to be exported

---

#### getPackageName

ExpressionTree

getPackageName()

Returns the name of the package to be exported.

getModuleNames

```java
List
<? extends
ExpressionTree
> getModuleNames()
```

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

**Returns:** the names of the modules to which the package is exported, or null

---

#### getModuleNames

List

<? extends

ExpressionTree

> getModuleNames()

Returns the names of the modules to which the package is exported,
or null, if the package is exported to all modules.

---

