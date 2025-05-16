.. _a7_diy:

===
DIY
===

After completing the lab, the player does DIY.

#. In the **DIY** interface:

   * Read the **DIY ACTIVITIES**.
   * Read the **SOLUTION VALIDATION METHOD**.

   .. image:: pictures/0001-diy-A7.png
      :alt: DIY interface showing activities and validation method instructions.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **RDS**.
   * Select **RDS**.

   .. image:: pictures/0002-diy-A7.png
      :alt: AWS console showing RDS service.
      :align: center
      :width: 600px

#. In the **Amazon RDS** interface:

   * Select **Databases**.

   .. image:: pictures/0003-diy-A7.png
      :alt: RDS dashboard showing Databases option.
      :align: center
      :width: 600px

#. In the **Databases** interface:

   * Select **my-database**.

   .. image:: pictures/0004-diy-A7.png
      :alt: RDS database list showing my-database selected.
      :align: center
      :width: 600px

#. In the **Databases** interface:

   * Select **Actions**.
   * Select **Create read replica**.

   .. image:: pictures/0005-diy-A7.png
      :alt: RDS database actions menu showing Create read replica option.
      :align: center
      :width: 600px

#. In the **Create read replica DB instance** interface:

   * In **DB instance class**, select **db.t3.xlarge-4 vCPU**.

   .. image:: pictures/0006-diy-A7.png
      :alt: Create read replica interface showing DB instance class selection.
      :align: center
      :width: 600px

#. In the **Create read replica DB instance** interface:

   * In **Multi-AZ deployment**, select **Yes**.

   .. image:: pictures/0007-diy-A7.png
      :alt: Create read replica interface showing Multi-AZ selection.
      :align: center
      :width: 600px

#. In the **Create read replica DB instance** interface:

   * In **Storage type**, select **General Purpose (SSD)**.

   .. image:: pictures/0008-diy-A7.png
      :alt: Create read replica interface showing Storage type selection.
      :align: center
      :width: 600px

#. In the **Network & Security** interface:

   * In **Destination region**, select **US East (N. Virginia)**.

   .. image:: pictures/0009-diy-A7.png
      :alt: Create read replica interface showing Destination region selection.
      :align: center
      :width: 600px

#. In the **Network & Security** interface:

   * In **Destination DB subnet group**, select **default-vpc**.

   .. image:: pictures/00010-diy-A7.png
      :alt: Create read replica interface showing Destination DB subnet group selection.
      :align: center
      :width: 600px

#. In the **Network & Security** interface:

   * In **Publicly accessible**, select **No**.

   .. image:: pictures/00011-diy-A7.png
      :alt: Create read replica interface showing Publicly accessible setting.
      :align: center
      :width: 600px

#. In the **Network & Security** interface:

   * In **VPC security groups**, select **default**.

   .. image:: pictures/00012-diy-A7.png
      :alt: Create read replica interface showing VPC security groups selection.
      :align: center
      :width: 600px

#. In the **RDS** interface (Create read replica):

   * In **Read replica source**, the source database ``my-database`` should be pre-filled.
   * In **DB instance identifier**, enter ``my-database-read-replica``.

   .. image:: pictures/00013-diy-A7.png
      :alt: Create read replica interface showing source and identifier fields.
      :align: center
      :width: 600px

#. In the **Database options** interface (Create read replica):

   * In **Database port**, enter ``3306``.
   * Select **Copy tags to snapshots**.

   .. image:: pictures/00014-diy-A7.png
      :alt: Create read replica interface showing database port and copy tags option.
      :align: center
      :width: 600px

#. In the **RDS** interface (Create read replica):

   * In **Monitoring**, uncheck **Disable enhanced monitoring**.
   * In **Performance Insights**, uncheck **Disable Performance Insights**.
   * In **Maintenance**, select **No**.
   * Select **Create read replica**.

   .. image:: pictures/00015-diy-A7.png
      :alt: Create read replica interface showing monitoring, PI, maintenance settings, and create button.
      :align: center
      :width: 600px
