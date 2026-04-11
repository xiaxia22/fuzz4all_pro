# Annotation Type Experimental

**Source:** `jdk.jfr\jdk\jfr\Experimental.html`

### Class Description

```java
@Inherited

@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
})
public @interface
Experimental
```

Annotation that specifies that an element is experimental and may change
without notice.

Clients that visualize Flight Recorder events should

not

show the
events or fields annotated with the

Experimental

annotation by
default. This annotation allows event producers the freedom to try out new
events without committing to them.

Clients may provide a check box (for example, in a preference page) where a
user can opt-in to display experimental data. If the user decide to do so,
the user interface should mark experimental events or fields so users can
distinguish them from non-experimental events.

This annotation is inherited.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type Experimental

```java
@Inherited

@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
})
public @interface
Experimental
```

Annotation that specifies that an element is experimental and may change
without notice.

Clients that visualize Flight Recorder events should

not

show the
events or fields annotated with the

Experimental

annotation by
default. This annotation allows event producers the freedom to try out new
events without committing to them.

Clients may provide a check box (for example, in a preference page) where a
user can opt-in to display experimental data. If the user decide to do so,
the user interface should mark experimental events or fields so users can
distinguish them from non-experimental events.

This annotation is inherited.

**Since:** 9

@Inherited

@Retention

(

RUNTIME

)

@Target

({

FIELD

,

TYPE

})
public @interface

Experimental

Annotation that specifies that an element is experimental and may change
without notice.

Clients that visualize Flight Recorder events should

not

show the
events or fields annotated with the

Experimental

annotation by
default. This annotation allows event producers the freedom to try out new
events without committing to them.

Clients may provide a check box (for example, in a preference page) where a
user can opt-in to display experimental data. If the user decide to do so,
the user interface should mark experimental events or fields so users can
distinguish them from non-experimental events.

This annotation is inherited.

Clients that visualize Flight Recorder events should

not

show the
events or fields annotated with the

Experimental

annotation by
default. This annotation allows event producers the freedom to try out new
events without committing to them.

Clients may provide a check box (for example, in a preference page) where a
user can opt-in to display experimental data. If the user decide to do so,
the user interface should mark experimental events or fields so users can
distinguish them from non-experimental events.

This annotation is inherited.

Clients may provide a check box (for example, in a preference page) where a
user can opt-in to display experimental data. If the user decide to do so,
the user interface should mark experimental events or fields so users can
distinguish them from non-experimental events.

This annotation is inherited.

This annotation is inherited.

---

