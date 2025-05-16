.. _a12_diy:

===
DIY
===

After completing the lab, the player does DIY.

Here’s the full set of steps:

#. In the **DIY** interface:

   * Read the **DIY ACTIVITIES**.
   * Read the **SOLUTION VALIDATION METHOD**.

   .. image:: pictures/0001-diy-A12.png
      :alt: DIY interface showing instructions.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Select **START LAB**.

   .. image:: pictures/0002-diy-A12.png
      :alt: DIY interface showing Start Lab button.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **EC2**.
   * Select **EC2**.

   .. image:: pictures/0003-diy-A12.png
      :alt: AWS Console showing EC2 service.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * Select the **lab/TravelAgencyWebServers** instance.
   * Select **Details** to view instance details.

   .. image:: pictures/0004-diy-A12.png
      :alt: EC2 interface navigating to view instance details.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Auto Scaling Groups**.
   * Select the **TravelAgencyWebServers** auto scaling group.
   * Select **Details** to see the details of the auto scaling group.

   .. image:: pictures/0005-diy-A12.png
      :alt: EC2 interface navigating to view ASG details.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Auto Scaling Groups**.
   * Select the **TravelAgencyWebServers** Auto Scaling Group.
   * Select **Instance management**.
   * View instance information.

   .. image:: pictures/0006-diy-A12.png
      :alt: EC2 interface navigating to view ASG instances.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Auto Scaling Groups**.
   * Select **TravelAgencyWebServers**.
   * Select **Details** to view the **Desired capacity**, **Minimum capacity**, and **Maximum capacity**.

   .. image:: pictures/0007-diy-A12.png
      :alt: EC2 interface showing ASG capacity details.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Auto Scaling Groups**.
   * Select the **TravelAgencyWebServers** Auto Scaling Group.
   * In the **Network** section, see the **Subnet ID** information.
   * In the **Load balancing** section, select **Edit**.

   .. image:: pictures/0008-diy-A12.png
      :alt: EC2 interface viewing ASG network info and selecting edit load balancing.
      :align: center
      :width: 600px

#. In the **Edit TravelAgencyWebServers** interface:

   * Select **Add a new load balancer**.

   .. image:: pictures/0009-diy-A12.png
      :alt: Edit ASG interface showing Add a new load balancer option.
      :align: center
      :width: 600px

#. In the **Load balancing** interface:

   * For **Load balancer type**, select **Application Load Balancer**.
   * For **Load balancer scheme**, select **Internet-facing**.

   .. image:: pictures/00010-diy-A12.png
      :alt: Load balancing interface showing ALB type and scheme selection.
      :align: center
      :width: 600px

#. In the **Edit TravelAgencyWebServers** interface:

   * In the **Availability Zones and subnets** section, select all 3 **AZ** and their corresponding subnets.

   .. image:: pictures/00011-diy-A12.png
      :alt: Edit ASG interface showing AZ and subnet selection.
      :align: center
      :width: 600px

#. In the **Edit TravelAgencyWebServers** interface:

   * In the **Default routing (forward to)** field, select **Create a target group**.

   .. image:: pictures/00012-diy-A12.png
      :alt: Edit ASG interface showing Create a target group option.
      :align: center
      :width: 600px

#. In the **Edit TravelAgencyWebServers** interface:

   * Select **Update**.

   .. image:: pictures/00013-diy-A12.png
      :alt: Edit ASG interface showing Update button.
      :align: center
      :width: 600px

#. In the **Auto Scaling Groups** interface:

   * View the update results.

   .. image:: pictures/00014-diy-A12.png
      :alt: Auto Scaling Groups interface showing update results.
      :align: center
      :width: 600px

#. In the **Auto Scaling Groups** interface:

   * Select the **TravelAgencyWebServers** Auto Scaling Group from the list.

   .. image:: pictures/00015-diy-A12.png
      :alt: Auto Scaling Groups interface showing ASG selected.
      :align: center
      :width: 600px

#. In the **Auto Scaling Groups** interface:

   * Select **Details** to see the details.

   .. image:: pictures/00016-diy-A12.png
      :alt: Auto Scaling Groups interface showing Details link.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Security Groups**.

   .. image:: pictures/00017-diy-A12.png
      :alt: EC2 interface showing Security Groups link.
      :align: center
      :width: 600px

#. In the **EC2 Security Groups** interface:

   * Select **Create security group**.

   .. image:: pictures/00018-diy-A12.png
      :alt: EC2 Security Groups interface showing Create security group button.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * For **Security group name**, enter ``TravelAgencyLoadBalancer``.

   .. image:: pictures/00019-diy-A12.png
      :alt: Create security group interface showing name field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * In the **Description** field, enter ``Allow access to the Travel Agency Load Balancer from the Internet``.

   .. image:: pictures/00020-diy-A12.png
      :alt: Create security group interface showing description field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * In the **VPC** field, select **lab/TravelAgencyVpc**.

   .. image:: pictures/00021-diy-A12.png
      :alt: Create security group interface showing VPC selection.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * In the **Inbound rules** section, select **Add rule**.

   .. image:: pictures/00022-diy-A12.png
      :alt: Create security group interface showing Add rule button.
      :align: center
      :width: 600px

#. In the **Create security group** interface (Rules):

   * In **Inbound rules**, select **HTTP** for the rule type.

   .. image:: pictures/00023-diy-A12.png
      :alt: Create security group inbound rules showing HTTP type selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface (Rules):

   * In **Outbound rules**, select **HTTP** for the rule type.

   .. image:: pictures/00024-diy-A12.png
      :alt: Create security group outbound rules showing HTTP type selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **Create security group**.

   .. image:: pictures/00025-diy-A12.png
      :alt: Create security group interface showing Create security group button.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Security Groups**.

   .. image:: pictures/00026-diy-A12.png
      :alt: EC2 interface showing Security Groups link.
      :align: center
      :width: 600px

#. In the **EC2 Security Groups** interface:

   * Select the **TravelAgencyWebServer** security group.

   .. image:: pictures/00027-diy-A12.png
      :alt: EC2 Security Groups interface showing TravelAgencyWebServer security group selected.
      :align: center
      :width: 600px

#. In the **EC2 Security Groups** interface:

   * Select **Actions**.

   .. image:: pictures/00028-diy-A12.png
      :alt: EC2 Security Groups interface showing Actions menu.
      :align: center
      :width: 600px

#. In the **Security Groups Actions** menu:

   * Select **Edit inbound rules**.

   .. image:: pictures/00029-diy-A12.png
      :alt: Security Groups Actions menu showing Edit inbound rules option.
      :align: center
      :width: 600px

#. In the **Edit inbound rules** interface:

   * Select **Delete** the existing rule.

   .. image:: pictures/00030-diy-A12.png
      :alt: Edit inbound rules interface showing delete option.
      :align: center
      :width: 600px

#. In the **Edit inbound rules** interface:

   * Select **Add rule**.

   .. image:: pictures/00031-diy-A12.png
      :alt: Edit inbound rules interface showing Add rule button.
      :align: center
      :width: 600px

#. In the **Edit Inbound rules** interface:

   * Select **HTTP**.

   .. image:: pictures/00032-diy-A12.png
      :alt: Edit inbound rules interface showing HTTP type selected.
      :align: center
      :width: 600px

#. In the **Edit Inbound rules** interface:

   * For **Source**, select **Custom**.
   * Select the **TravelAgencyLoadBalancer** security group.

   .. image:: pictures/00033-diy-A12.png
      :alt: Edit inbound rules interface showing source security group selected.
      :align: center
      :width: 600px

#. In the **Edit Inbound rules** interface:

   * Select **Save rules**.

   .. image:: pictures/00034-diy-A12.png
      :alt: Edit inbound rules interface showing Save rules button.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Load Balancers**.

   .. image:: pictures/00035-diy-A12.png
      :alt: EC2 interface showing Load Balancers link.
      :align: center
      :width: 600px

#. In the **EC2 Load Balancers** interface:

   * Select the **TravelAgencyWebServers-1** Load Balancer.

   .. image:: pictures/00036-diy-A12.png
      :alt: EC2 Load Balancers interface showing ALB selected.
      :align: center
      :width: 600px

#. In the **Load Balancer** interface:

   * Select **Description** to view description information.

   .. image:: pictures/00037-diy-A12.png
      :alt: Load Balancer interface showing Description link.
      :align: center
      :width: 600px

#. In the **Load Balancer** interface:

   * Select **Edit security groups**.

   .. image:: pictures/00038-diy-A12.png
      :alt: Load Balancer interface showing Edit security groups link.
      :align: center
      :width: 600px

#. In the **Edit security groups** interface:

   * Select the **TravelAgencyLoadBalancer** security group to add it.

   .. image:: pictures/00039-diy-A12.png
      :alt: Edit security groups interface showing TravelAgencyLoadBalancer security group selected.
      :align: center
      :width: 600px

#. In the **Edit security groups** interface:

   * Uncheck the **TravelAgencyWebServer** security group to remove it.

   .. image:: pictures/00040-diy-A12.png
      :alt: Edit security groups interface showing TravelAgencyWebServer security group unchecked.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Load Balancers**.

   .. image:: pictures/00041-diy-A12.png
      :alt: EC2 interface showing Load Balancers link.
      :align: center
      :width: 600px

#. In the **EC2 Load Balancers** interface:

   * Select the **TravelAgencyWebServer-1** Load Balancer.

   .. image:: pictures/00042-diy-A12.png
      :alt: EC2 Load Balancers interface showing ALB selected.
      :align: center
      :width: 600px

#. In the **Load Balancer** interface:

   * In the **Description** section, view and copy the **DNS name**.

   .. image:: pictures/00043-diy-A12.png
      :alt: Load Balancer interface showing DNS name to copy.
      :align: center
      :width: 600px

#. Open a web browser.

   .. image:: pictures/00044-diy-A12.png
      :alt: Web browser opened.
      :align: center
      :width: 600px

#. Paste the **DNS name** into the browser's address bar.

   .. image:: pictures/00045-diy-A12.png
      :alt: Browser showing DNS name pasted.
      :align: center
      :width: 600px

#. Select **Enter** and view the interface.

   .. image:: pictures/00046-diy-A12.png
      :alt: Browser showing Enter key pressed.
      :align: center
      :width: 600px

#. In the browser:

   * Append ``/health`` to the end of the **DNS name** in the address bar.

   .. image:: pictures/00047-diy-A12.png
      :alt: Browser showing /health added to the DNS name.
      :align: center
      :width: 600px

#. In the browser:

   * View the results displayed.

   .. image:: pictures/00048-diy-A12.png
      :alt: Browser showing health check results.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Target Groups**.

   .. image:: pictures/00049-diy-A12.png
      :alt: EC2 interface showing Target Groups link.
      :align: center
      :width: 600px

#. In the **EC2 Target Groups** interface:

   * Select the **TravelAgencyWebServers** target group.

   .. image:: pictures/00050-diy-A12.png
      :alt: EC2 Target Groups interface showing target group selected.
      :align: center
      :width: 600px

#. In the **Target Group** interface:

   * Select **Health checks**.

   .. image:: pictures/00051-diy-A12.png
      :alt: Target Group interface showing Health checks link.
      :align: center
      :width: 600px

#. In the **Edit health check settings** interface:

   * In the **Health check path** field, enter ``/health``.
   * Select **Advanced health check settings**.

   .. image:: pictures/00052-diy-A12.png
      :alt: Edit health check settings interface showing path and advanced settings link.
      :align: center
      :width: 600px

#. In the **Advanced health check settings** interface:

   * In **Unhealthy threshold**, enter ``2``.
   * In **Timeout**, enter ``2``.
   * In **Interval**, enter ``5``.
   * Select **Save changes**.

   .. image:: pictures/00053-diy-A12.png
      :alt: Advanced health check settings interface showing thresholds, timeout, interval, and save.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Paste **TravelAgencyWebServers-1** into the **Your ALB name** field.
   * Paste **TravelAgencyWebServers** into the **Your Auto Scaling group name** field.
   * Select **VALIDATE**.
   * View the **VALIDATION MESSAGE** which should show **Success! All 3 Availability Zones are covered by instances behind a Load Balancer**.
   * Select **EXIT** to return to the city interface.

   .. image:: pictures/00054-diy-A12.png
      :alt: DIY interface showing validation input, success message, and exit.
      :align: center
      :width: 600px

#. In the **city interface**:

   * Select **ASSIGNMENTS**.
   * Select **COLLECT**.
   * Select **NEXT**.
   * Select **COLLECT**.

   .. image:: pictures/00055-diy-A12.png
      :alt: City interface showing collection steps.
      :align: center
      :width: 600px

#. **Congratulations to the player receiving the reward!**
