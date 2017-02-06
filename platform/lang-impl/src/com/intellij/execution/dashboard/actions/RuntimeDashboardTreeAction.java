/*
 * Copyright 2000-2017 JetBrains s.r.o.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.intellij.execution.dashboard.actions;

import com.intellij.execution.dashboard.*;
import com.intellij.openapi.actionSystem.AnActionEvent;
import org.jetbrains.annotations.NotNull;

import javax.swing.*;

/**
 * @author konstantin.aleev
 */
public abstract class RuntimeDashboardTreeAction<T extends DashboardNode> extends DashboardTreeAction<T, RuntimeDashboardContent> {
  protected RuntimeDashboardTreeAction(String text, String description, Icon icon) {
    super(text, description, icon);
  }

  @Override
  protected final RuntimeDashboardContent getTreeContent(AnActionEvent e) {
    return e.getData(RuntimeDashboardContent.KEY);
  }

  @Override
  protected boolean isVisibleForAnySelection(@NotNull AnActionEvent e) {
    return true;
  }
}
